from django.conf import settings

def facebook_common(request):
    return {
        'FACEBOOK_APP_ID'  : settings.FACEBOOK_APP_ID,
    }
