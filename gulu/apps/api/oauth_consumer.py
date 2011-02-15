from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from piston.models import Sync, Site
from urllib import urlencode
import cgi
import external_apps.oauth2 as oauth


@login_required
def oauth_ask_approve(request, site_name = None): 
    """
    Don't need database support, it's a service by oauth2.
    It can help user(Consumer) generate signature.    
    """
    #site_name = request.GET.get('site')
    
    site_o = get_object_or_404(Site, name = site_name)
    sync_list = Sync.objects.filter(site=site_o, user = request.user)
    if sync_list:
        return HttpResponseRedirect("http://localhost:8000/api/tweet_a_message")
    
    
    consumer = oauth.Consumer(site_o.key, site_o.secret)
    client = oauth.Client(consumer)
    resp, content = client.request(site_o.request_url, "GET")
    if resp['status'] != '200':
        print content
        raise Exception("Invalid response %s." % resp['status'])    
    """
    As one uses 'client.request' to request 'request_token',
    the one who provides service will check out if the request is valid.
    The Service Provider will use the information you sent to it to 
    'regenerate' your oauth_signature, and confirm them.
    Since there is no one knows your 'CONSUMER_SECRET' except you and the Service Provider,
    (and you will not send your 'CONSUMER_SECRET' with HTTP request,)
    therefore it is a safe way to authorize your identity.
    An Example: CONSUMER_KEY='appkey', CONSUMER_SECRET='appsec'
        oauth_nonce=46137579
        oauth_timestamp=1296094410
        oauth_consumer_key=appkey
        oauth_signature_method=HMAC-SHA1
        oauth_version=1.0
        oauth_signature=uekzn2aETpsH0USE53DYUwH6Zww=
    """
    request_token = dict(cgi.parse_qsl(content))
    #callback_address = 'http://gulu.demo.gd/api/oauth_handle_token/%s/' % (site_o.name)
    #callback_address = 'http://localhost:8000/api/oauth_handle_token/%s/' % (site_o.name)
    sync_o = Sync(user = request.user, site = site_o, token = request_token['oauth_token'], token_secret = request_token['oauth_token_secret'])
    sync_o.save()
    #print 'request_token:', request_token    
    address = "%s?oauth_token=%s" % (site_o.authorize_url, sync_o.token)
    return HttpResponseRedirect(address)


def oauth_handle_token(request,site_name=None):
    error_msg = ''
    if request.GET.get('error'):
        error_msg = request.GET.get('error')
        return render_to_response('oauth_success.html', {
        'site_name' : site_name,
        'error_msg': error_msg,
        }, context_instance = RequestContext(request))        
    
    site_o = get_object_or_404(Site, name = site_name)
    
    #confirmed = request.GET.get('oauth_callback_confirmed')
    #oauth_verifier = request.GET.get('oauth_verifier')
    try:
        sync_o = get_object_or_404(Sync, token = request.GET.get('oauth_token'))
    except Http404:
        error_msg = 'The token information is not correct.'
        return render_to_response('oauth_success.html', {
        'site_name' : site_name,
        'error_msg': error_msg,
        }, context_instance = RequestContext(request))
    sync_o.verifier = request.GET.get('oauth_verifier')    
    sync_o.save()
    """
    Create token by oauth.Token, and then put them into oauth.Client,
    so that Oauth2 will generate "oauth request" for access_token.
    Like this one:
        oauth_nonce=21479729
        oauth_timestamp=1296094414
        oauth_signature_method=MAC-SHA1
        oauth_consumer_key=appkey
        oauth_verifier=CY2J3DP6fN
        oauth_version=1.0
        oauth_token=ThNVYzS8yrLF3FfGps
        oauth_signature=KP+zim+9CXq0plXaYMKSKU3BoJY=
    """
    consumer = oauth.Consumer(site_o.key, site_o.secret)
    token = oauth.Token(sync_o.token, sync_o.token_secret)
    token.set_verifier(sync_o.verifier)    
    client = oauth.Client(consumer, token)
    resp, content = client.request(site_o.access_url, "POST")
    access_token = dict(cgi.parse_qsl(content))
    #oauth.Request.from_consumer_and_token
    """
    Get Access token finally:
        oauth_token_secret=7UbBcEwgpKXtG3tqBzAtfrNNjS8LaEMg
        oauth_token=EsV3ndFsP96jM9LSpf',
    Then modify the 'sync' with access_token, and set 'is_access' = True 
    """
    sync_o.token = access_token['oauth_token']
    sync_o.token_secret = access_token['oauth_token_secret']
    sync_o.is_access = True
    sync_o.save()
    return render_to_response('oauth_success.html', {
        'site_name' : site_name,
        'error_msg': error_msg,
    }, context_instance = RequestContext(request))