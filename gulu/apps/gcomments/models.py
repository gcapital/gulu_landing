""" Gulu-specific comments module models """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: models.py 417 2010-12-21 06:01:53Z ben $"

from django.db import models
from django.contrib.comments.models import Comment

from user_profiles.models import UserProfile

class GComment(Comment):
	""" Gulu-specific comment, customized from built-in comments model """
	
	commenter = models.ForeignKey('user_profiles.UserProfile', blank=True, null=True, related_name="%(class)s_comments")

	def save(self, *args, **kwargs):
		if self.user:
			self.commenter = UserProfile.objects.get(pk=self.user.id)
		super(GComment, self).save(*args, **kwargs)
