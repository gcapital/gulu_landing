import datetime
from django.db import models

# Create your models here.
class NewsletterUser(models.Model):
    username        = models.CharField(max_length=30, null=False)
    email           = models.EmailField(max_length=75, null=False)
    created         = models.DateTimeField(default=datetime.datetime.now)
    
    def __unicode__(self):
        return self.username
