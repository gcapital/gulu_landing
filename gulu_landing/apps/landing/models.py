from django.db import models

class Registration(models.Model):
    email = models.EmailField(max_length=100)

    def __unicode__(self):
        return self.email

