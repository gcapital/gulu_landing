# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def request_token_ready(request, token):
    error = request.GET.get('error', '')
    ctx = RequestContext(request, {
        'error' : error,
        'token' : token,
        'verifier' : token.verifier
    })
    return render_to_response(
        'Oauth_verifier.html',
        context_instance = ctx
    )