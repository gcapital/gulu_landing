from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django import forms
from piston.models import Sync, Site
import cgi
import oauth2 as oauth


class MessageForm(forms.Form):
    message = forms.CharField(max_length=100)
    
@login_required
def tweet_a_message(request):
    
    if request.method == 'POST':
        site_name = 'twitter'
        site_o = get_object_or_404(Site, name = site_name)
        sync_o = get_object_or_404(Sync, site = site_o, user = request.user) 
        consumer = oauth.Consumer(site_o.key, site_o.secret)
        token = oauth.Token(sync_o.token, sync_o.token_secret)  
        uri = 'http://api.twitter.com/1/statuses/update.json'  
        client = oauth.Client(consumer, token)
        form = MessageForm(request.POST)
        if form.is_valid():
            message = 'status="%s"'%form.cleaned_data['message']
            resp, content = client.request(uri, "POST", body=message)            
    else:
        content = ''
        form = MessageForm()
        
    return render_to_response('tweet_test.html', {
    'form' : form,
    'content': content,
    }, context_instance = RequestContext(request))

    
    
    