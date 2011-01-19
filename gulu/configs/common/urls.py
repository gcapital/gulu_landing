from django.conf.urls.defaults import *
from django.conf import settings

# Customized Error pages
handler404 = 'globals.views.redirect404'

urlpatterns = patterns('',
    url( r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True} ),  
    url( r'^$', 'globals.views.home', name = "globals-home" ),
)
