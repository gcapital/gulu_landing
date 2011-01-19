from django.conf.urls.defaults import *
from django.conf import settings

# Customized Error pages
#from globals import views
#handler404 = views.newsletter
#handler500 = views.newsletter

urlpatterns = patterns('',
    url( r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True} ),  
    url( r'^$', 'globals.views.home', name = "globals-home" ),
)
