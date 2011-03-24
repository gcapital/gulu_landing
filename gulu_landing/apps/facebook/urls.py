from django.conf.urls.defaults import *

urlpatterns = patterns('facebook.views',
   url(r'^connect/$', 'connect', name='facebook-connect'),
)

