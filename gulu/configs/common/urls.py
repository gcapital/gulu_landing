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
    # url( r'^$', 'globals.views.home', name = "globals-home" ),
    # url( r'^signup/$', 'globals.views.signup', name = "globals-signup" ),
    # url( r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'globals_login.html'}, name = "globals-login" ),
    # url( r'^logged_in/$', 'globals.views.logged_in', name = "globals-logged-in" ),
    # url( r'^logout/$', 'django.contrib.auth.views.logout_then_login', name = "globals-logout" ),
    # url( r'^forgot-password/$', 'globals.views.forgot_password', name = "globals-forgot-password" ),
    #  
    # # Module views
    # ( r'^comments/', include( 'django.contrib.comments.urls' ) ),
    # ( r'^dish/', include( 'dish.urls' ) ),
    # ( r'^deal/', include( 'deal.urls' ) ),
    # ( r'^invite/', include( 'invite.urls' ) ),
    # ( r'^like/', include('like.urls')),
    # ( r'^mission/', include( 'mission.urls' ) ),
    # ( r'^photos/', include( 'photos.urls' ) ),
    # ( r'^restaurant/', include( 'restaurant.urls' ) ),
    # #( r'^globals/', include( 'globals.urls' ) ),
    # ( r'^review/', include( 'review.urls' ) ),
    # ( r'^users/', include( 'user_profiles.urls' ) ),
    # ( r'^wall/', include( 'wall.urls' ) ),
    # ( r'^recommend/', include( 'recommend.urls' ) ),
    (r'^search/', include('search.urls')),
    (r'^api/', include('api.urls')),
    # Template test view
    # url( r'^test/$', 'django.views.generic.simple.direct_to_template', {'template': 'test.html'} ),
    
    # Catchall for profile/restaurant views
 )
