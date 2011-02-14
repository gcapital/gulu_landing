""" Gulu wall module views """

__author__="Peter Song <peter.song@geniecapital.com>"
__version__="$Id: models.py 580 2011-01-27 03:45:09Z ben $:"

import datetime

from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models

class WallPost(models.Model):
	poster = models.ForeignKey("user_profiles.UserProfile")
	content = models.TextField()
	photo = models.ForeignKey("photos.Photo", null=True, blank=True)
	owner_content_type = models.ForeignKey(ContentType, related_name="owner")
	owner_object_id = models.PositiveIntegerField() 
	owner = generic.GenericForeignKey("owner_content_type","owner_object_id")
	created = models.DateTimeField(default=datetime.datetime.now)

	def __unicode__( self ):
		return "%s -> %s: %s" % (self.poster, self.owner, self.content)

	class Meta:
		ordering=["-created"]

#def action_handler(sender, instance, created, **kwargs):
#	if created:
#		action.send(instance.poster, verb="posted on", target=owner)
#post_save.connect(action_handler, WallPost)
