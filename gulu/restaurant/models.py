""" Gulu restaurant models """

__author__ = "Gage Tseng <gage.tseng@geniecapital.com>"
__version__ = "$Id: models.py 570 2011-01-26 07:39:21Z gage $"

import datetime

from django.db import models

class Restaurant(models.Model):
	name				= models.CharField(max_length=100)
	slug				= models.SlugField(max_length=100, unique=True, null=True, blank=True)
	address				= models.CharField(max_length=255)
	city				= models.CharField(max_length=50)
	region				= models.CharField(max_length=50)
	phone				= models.CharField(max_length=50, null=True, blank=True)
	type				= models.ForeignKey('RestaurantType')
	description			= models.TextField()
	business_hours		= models.TextField(null=True, blank=True)
	transportation		= models.TextField(null=True, blank=True)
	services			= models.ManyToManyField('RestaurantService', blank=True, null=True)
	note				= models.TextField(null=True, blank=True)
	score				= models.FloatField(null=True, blank=True)
	can_upload_dish		= models.BooleanField(default=True)
	#best_photos			= models.ManyToManyField('photos.RestaurantPhoto', related_name="restaurant_best_photos", null=True, blank=True)
	best_reviews		= models.ManyToManyField('review.Review', related_name="restaurant_best_reviews", blank=True, null=True)
	#best_video			 = models.ManyToManyField('video.Video', blank=True, null=True)
	#location_group_id	= models.IntegerField(default=0)
	managers			= models.ManyToManyField('user_profiles.UserProfile', blank=True, null=True)
	rating_food			= models.IntegerField(default=0)
	rating_atmosphere	= models.IntegerField(default=0)
	rating_service		= models.IntegerField(default=0)
	rating_price		= models.IntegerField(default=0)
	follower_count		= models.IntegerField(default=0)
	longitude			= models.FloatField(default=0)
	latitude			= models.FloatField(default=0)
	created				= models.DateTimeField(default=datetime.datetime.now)
	count_recommend		= models.IntegerField(default=0)
	profile_pics		= models.ManyToManyField('photos.Photo', related_name='restaurant_profile_pics', blank=True, null=True)
	main_profile_pic	= models.ForeignKey('photos.Photo', related_name='restaurant_profile_pic', blank=True, null=True)
	best_photos			= models.ManyToManyField('photos.Photo', related_name='best_photo_restaurant', blank=True, null=True)
	location_group_id	= models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.name;
	
	
	class Meta:	
		permissions = (
            ('manage_restaurant', 'Can manage Restaurant'),
        )

class RestaurantService(models.Model):
	name				= models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.name


class RestaurantRating(models.Model):
	user			= models.ForeignKey('user_profiles.UserProfile')
	restaurant		= models.ForeignKey('Restaurant')
	is_delicious	= models.BooleanField()
	good_atmosphere = models.BooleanField()
	good_service	= models.BooleanField()
	good_price		= models.BooleanField()
	ip_address		= models.CharField(max_length=15)
	location		= models.CharField(max_length=255)
	created			= models.DateTimeField(default=datetime.datetime.now)
	
	def __unicode__(self):
		return self.restaurant.name;

class Vip(models.Model):
	restaurant			 = models.ForeignKey('Restaurant')
	reserve				 = models.BooleanField()
	delivery			 = models.BooleanField()
	delivery_free		 = models.BooleanField()
	takeout				 = models.BooleanField()
	order_online_dis	 = models.BooleanField()
	order_online_dis_v	 = models.BooleanField()
	restaurant_dis		 = models.BooleanField()
	restaurant_dis_v	 = models.BooleanField()
	reserve_online_dis	 = models.BooleanField()
	reserve_online_dis_v = models.BooleanField()
	other				 = models.BooleanField()
	other_description	 = models.CharField(max_length=255)
	price_1m			 = models.FloatField()
	price_3m			 = models.FloatField()
	price_6m			 = models.FloatField()
	price_12m			 = models.FloatField()
	active				 = models.BooleanField()
	created				 = models.DateTimeField(default=datetime.datetime.now)
	
	def __unicode__(self):
		return self.restaurant.name+' active='+self.active;


class RestaurantType(models.Model):
	name	= models.CharField(max_length=75)

	def __unicode__(self):
		return self.name;


class Chef(models.Model):
	restaurant			= models.ForeignKey('Restaurant')
	name				= models.CharField(max_length=50)
	description			= models.TextField()
	priority			= models.SmallIntegerField()
	created				= models.DateTimeField(default=datetime.datetime.now)
	
	def __unicode__(self):
		return self.restaurant.name+' name='+self.name