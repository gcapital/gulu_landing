from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Customized Error pages
from globals import views
#handler404 = 'globals.views.redirect404'
handler404 = views.handler404
handler500 = views.handler500

urlpatterns=patterns( '',
    # Example:
    # (r'^gulu/', include('gulu.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    #( r'^admin/doc/', include( 'django.contrib.admindocs.urls' ) ),

    # Uncomment the next line to enable the admin:
    ( r'^admin/', include( admin.site.urls ) ),

    # Static media - dev only
    url( r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True} ),

    # Non-module views
 
    # Module views
    (r'^api/', include('api.urls')),
    # Template test view

    
    # Catchall for profile/restaurant views
 )
