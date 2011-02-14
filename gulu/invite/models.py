""" Gulu invite module models """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: models.py 388 2010-12-16 06:59:01Z ben $"

import datetime

from django.db import models

class Invite(models.Model):
	restaurant			= models.ForeignKey('restaurant.Restaurant')
	title				= models.CharField(max_length=100, null=True, blank=True)
	start_time			= models.DateTimeField()
	message				= models.TextField(null=True, blank=True)
	inviter				= models.ForeignKey('user_profiles.UserProfile')
	total_user_sms		= models.IntegerField()
	total_other_sms		= models.IntegerField()
	total_user_invite	= models.IntegerField()
	#reservation		= models.ForeignKey('reservations')
	created				= models.DateTimeField(default=datetime.datetime.now)

class InviteList(models.Model):
	invite	= models.ForeignKey('Invite')
	user	= models.ForeignKey('user_profiles.UserProfile', null=True, blank=True)
	email	= models.CharField(max_length=100)
	sms		= models.CharField(max_length=50)
