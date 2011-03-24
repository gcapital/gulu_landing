from django.db import models
from django.contrib.auth.models import User

from djangotoolbox.fields import ListField

class FacebookProfile(models.Model):
    """ Links a facebook profile to a user profile """
    user = models.OneToOneField(User)
    facebook_id = models.IntegerField(null=True, blank=True)
    friend_ids = ListField(models.CharField(max_length=100), null=True, blank=True)
    access_token = models.CharField(max_length=100)
    
    def __unicode__(self):
       return self.user.__unicode__()
