""" Gulu follow module models """

from django.db import models
from django.conf import settings
from django.contrib.auth import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey

USER_MODEL = getattr(settings, "CUSTOM_USER_MODEL", User)

class Follow(models.Model):
	user = models.ForeignKey(USER_MODEL)
	content_type = models.ForeignKey(ContentType, null=True, blank=True)
	object_id = models.PositiveIntegerField(null=True, blank=True)
	content_object = GenericForeignKey()
	
	class Meta:
		pass