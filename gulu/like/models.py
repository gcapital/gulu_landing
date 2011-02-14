""" Gulu like module models """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id$"

import datetime

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey

user_model = getattr(settings, 'CUSTOM_USER_MODEL', User)

class LikeManager(models.Manager):

	def like(self, user, content_object):
		if not self.does_like(user, content_object):
			self.create(user=user, content_object=content_object)		
		return True
	
	def unlike(self, user, content_object):
		content_type = ContentType.objects.get_for_model(content_object)
		if self.does_like(user, content_object):
			like = self.get(user=user, content_type=content_type,
						 object_id=content_object.id)
			like.delete()
		return True
	
	def does_like(self, user, content_object):
		content_type = ContentType.objects.get_for_model(content_object)
		return self.filter(user=user, content_type=content_type, 
						   object_id=content_object.id).count() > 0
		
	def liked_objects_for(self, user):
		return set([obj.content_object for obj in self.filter(user=user)])
	
class Like(models.Model):
	user = models.ForeignKey(user_model)
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey()
	created = models.DateTimeField(default=datetime.datetime.now)

	objects = LikeManager()

	class Meta:
		ordering = ['-created']
		unique_together = ("user", "content_type", "object_id")

	def __unicode__(self):
		return "%s likes %s" % (self.user, self.content_object)
