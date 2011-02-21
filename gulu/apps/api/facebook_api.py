"""PISTON LIB"""
from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, require_mime, require_extended
from piston.models import Sync, Site
"""GULU LIB"""
from user_profiles.models import UserProfile
from photos.models import Photo
"""DJANGO LIB"""
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django import forms
from django.db.models import FileField
""""PYTHON LIB"""
from urllib import urlencode
import httplib2, cgi, urllib2, json
import oauth2 as oauth
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

"""GLOBAL VARIATION"""
class MessageForm(forms.Form):
    message = forms.CharField(max_length=100)
    photo_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    photo_url = forms.CharField(widget=forms.HiddenInput(), required=False)


PTEST=False

REDIRECT_URI_ACCESS = 'http://api.gulu.com/api/oauth_facebook_access'
FACEBOOK_SCOPE = 'publish_stream,read_stream,user_status,user_videos,user_events,user_photos,email,user_groups,offline_access'

#ask facebook auth
def oauth_facebook_request(request):
    
    site_o = get_object_or_404(Site, name = 'facebook')
    uid = request.POST.get('uid')
    if PTEST:
        uid = request.GET.get('uid')
    user_o = get_object_or_404(UserProfile, id=uid)
    sync_list = Sync.objects.filter(site=site_o, user = user_o)
    if sync_list:
        if sync_list[0].is_access:            
            return render_to_response('facebook_cancel.html', {
                   'uid':uid,
                   }, context_instance = RequestContext(request))
            
    facebook_url = "https://www.facebook.com/dialog/oauth?"    
    data = {'client_id':site_o.key,'redirect_uri':REDIRECT_URI_ACCESS+'?uid=%s'%uid, 
            'scope':FACEBOOK_SCOPE}
    parameter = urlencode(data)
    url = facebook_url+parameter
    return HttpResponseRedirect(url)
  
def oauth_facebook_access(request):
    if request.GET.get('code'):
        code = request.GET.get('code')
    else: 
        raise Http404
    uid = request.GET.get('uid')
    user_o = get_object_or_404(UserProfile, id=uid)
    site_o = get_object_or_404(Site, name = 'facebook')
    sync_o = Sync(user=user_o, site = site_o, token_secret = code)
    facebook_url = 'https://graph.facebook.com/oauth/access_token?'
    data = {'client_id':site_o.key,'redirect_uri':REDIRECT_URI_ACCESS+'?uid=%s'%uid,
            'client_secret':site_o.secret,'code':code}
    parameter = urlencode(data)
    
    url = facebook_url+parameter
    h = httplib2.Http()
    resp, content = h.request(url, "GET")
    resp_dict = dict(cgi.parse_qsl(content))
    sync_o.is_access = True
    sync_o.token = resp_dict['access_token']    

    #Get user facebook id for further usage
    url = 'https://graph.facebook.com/me?access_token=%s'%resp_dict['access_token']
    h = httplib2.Http()
    resp, content = h.request(url, "GET")
    user_pro = json.loads(content)
    sync_o.verifier = user_pro['id']
    sync_o.save()
    user_o.syncs.add(sync_o)
    error_msg = None
    
    
    return render_to_response('facebook_oauth_end.html', {
        'message' : 'oauth finish',
    }, context_instance = RequestContext(request))

#http://localhost:8000/api/facebook_postwall

def facebook_cancel(request):    
    message = request.POST.get('submit')
    if message == 'YES':
        uid = request.POST.get('uid')
        user_o = UserProfile.objects.get(id=uid)
        sync_o = Sync.objects.get(user=uid,site__name='facebook')
        user_o.syncs.remove(sync_o)
        sync_o.delete()
    return render_to_response('facebook_oauth_end.html', 
                                {'message':message},
                               context_instance = RequestContext(request))
        
    
        


def facebook_postwall(request):
    if request.method == 'POST':
        site_o = get_object_or_404(Site, name = 'facebook')
        sync_o = get_object_or_404(Sync, user=request.user, site = site_o)        
        url = 'https://graph.facebook.com/%s/photos?access_token=%s'%(sync_o.verifier,sync_o.token)          
        form = MessageForm(request.POST)
        if form.is_valid():
            register_openers()
            photo_o = get_object_or_404(Photo, id = form.cleaned_data['photo_id'])
            #Use "Poster" to upload photos or files                     
            datagen, headers = multipart_encode({"source": open(photo_o.image.path, "rb"),
                                                 'message':form.cleaned_data['message'].encode('utf-8')})
            req = urllib2.Request(url, datagen, headers)
            photo_id = urllib2.urlopen(req).read()
    else:
        form = MessageForm()
        
    return render_to_response('facebook_test.html', {
    'form' : form,
    }, context_instance = RequestContext(request))
        
    
