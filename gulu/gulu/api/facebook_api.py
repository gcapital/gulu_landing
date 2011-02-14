from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django import forms
from django.db.models import FileField
from piston.models import Sync, Site
from photos.models import Photo
from urllib import urlencode
import httplib2, cgi, urllib2, json
import external_apps.oauth2 as oauth
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

class MessageForm(forms.Form):
    message = forms.CharField(max_length=100)
    photo_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    photo_url = forms.CharField(widget=forms.HiddenInput(), required=False)    


"""
1. http://localhost:8000/api/oauth_facebook_request
2. http://localhost:8000/api/oauth_facebook_access
"""
@login_required
def oauth_facebook_request(request):
    site_o = get_object_or_404(Site, name = 'facebook')
    sync_list = Sync.objects.filter(site=site_o, user = request.user)
    if sync_list:
        return HttpResponseRedirect("http://localhost:8000/api/facebook_error")
    facebook_url = "https://www.facebook.com/dialog/oauth?"    
    data = {'client_id':site_o.key,'redirect_uri':'http://gulu.com/', 
            'scope':'publish_stream,read_stream,user_status,user_videos,user_events,user_photos,email,user_groups,offline_access'}
    parameter = urlencode(data)
    url = facebook_url+parameter
    return HttpResponseRedirect(url)

@login_required    
def oauth_facebook_access(request):
    if request.GET.get('code'):
        code = request.GET.get('code')
    else: 
        raise Http404
    site_o = get_object_or_404(Site, name = 'facebook')
    sync_o = Sync(user=request.user, site = site_o, verifier = code)
    facebook_url = 'https://graph.facebook.com/oauth/access_token?'
    data = {'client_id':site_o.key,'redirect_uri':'http://gulu.com/',
            'client_secret':site_o.secret,'code':code}
    parameter = urlencode(data)
    
    url = facebook_url+parameter
    h = httplib2.Http(".cache")
    resp, content = h.request(url, "GET")
    resp_dict = dict(cgi.parse_qsl(content))
    sync_o.is_access = True
    sync_o.token = resp_dict['access_token']    

    #Get user id
    url = 'https://graph.facebook.com/me?access_token=%s'%resp_dict['access_token']
    h = httplib2.Http(".cache")
    resp, content = h.request(url, "GET")
    user_pro = json.loads(content)
    sync_o.type_id = user_pro['id']
    sync_o.save()
    error_msg = None
    
    
    return render_to_response('oauth_success.html', {
        'site_name' : 'facebook',
        'error_msg': error_msg,
    }, context_instance = RequestContext(request))

#http://localhost:8000/api/facebook_postwall
@login_required    
def facebook_postwall(request):
    if request.method == 'POST':
        site_o = get_object_or_404(Site, name = 'facebook')
        sync_o = get_object_or_404(Sync, user=request.user, site = site_o)        
        url = 'https://graph.facebook.com/%s/photos?access_token=%s'%(sync_o.type_id,sync_o.token)          
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
    