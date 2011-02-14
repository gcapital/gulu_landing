""" Gulu blog module models """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: models.py 571 2011-01-26 07:50:47Z ben $"

import datetime

from django.db import models

from bbcode.fields import BBCodeTextField

class BasePost(models.Model):
	poster		= models.ForeignKey('user_profiles.UserProfile')
	title		= models.CharField(max_length=255)
	created		= models.DateTimeField(default=datetime.datetime.now)
	content		= BBCodeTextField()
	
	class Meta:
		abstract = True
	
	def __unicode__(self):
		return self.title
	
class RestaurantPost(BasePost):
	restaurant = models.ForeignKey('restaurant.Restaurant', related_name="posts")

class UserPost(BasePost):
	owner = models.ForeignKey('user_profiles.UserProfile', related_name="posts")

	def get_absolute_url(self):
		return "/users/%s/blog/%s/" % (self.poster.id, self.id)