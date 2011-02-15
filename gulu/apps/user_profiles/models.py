""" User profile models """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: models.py 624 2011-01-31 02:10:55Z peter $"

import datetime

from django.db import models
from django.contrib.auth.models import User, UserManager
from django.utils.translation import ugettext_lazy as _

class UserProfile(User):
	""" User profile model
	
	This model inherits from the built-in user object to facilitate authentication,
	user creation, and administration.
	
	Any models in other apps which contain foreign keys to users should instead
	use this model.
	"""

	GENDER_MALE = 1
	GENDER_FEMALE = 2
	GENDER_CHOICES = [
		(GENDER_MALE, _("Male")),
		(GENDER_FEMALE, _("Female")),
	]

	slug				 = models.SlugField(max_length=100, unique=True, null=True, blank=True)
	birthday			 = models.DateField(null=True, blank=True)
	gender				 = models.IntegerField(null=True, blank=True, choices=GENDER_CHOICES)
	nickname			 = models.CharField(max_length=50, null=True, blank=True)
	profile_pics		 = models.ManyToManyField('photos.Photo', null=True, blank=True, related_name='user_profile_pics')
	main_profile_pic	 = models.ForeignKey('photos.Photo', null=True, blank=True, related_name='user_main_profile_pic')
	about_me    		 = models.TextField(null=True, blank=True)
	favorite_count		 = models.PositiveIntegerField(default=0)
	follower_count		 = models.PositiveIntegerField(default=0)
	following_count		 = models.PositiveIntegerField(default=0)
	gulu_points			 = models.FloatField(default=5)
	phone				 = models.CharField(max_length=20, null=True)
	phone_country		 = models.CharField(max_length=6, null=True)
	syncs		 	     = models.ManyToManyField('piston.Sync', null=True, blank=True, related_name='user_profile_syncs')

	# TODO: Add remaining fields from old MySQL schema

	# Use the built-in UserManager for access to create_user methods, etc.
	objects = UserManager()

	def get_full_name(self):
		return "%s %s" % (self.first_name, self.last_name)

	def get_absolute_url(self):
		if self.slug:
			return "/%s/" % self.slug
		else:
			return "/users/%s/" % self.id
