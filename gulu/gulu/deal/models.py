""" Gulu deal module models """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: models.py 579 2011-01-27 03:44:21Z jason $"

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Deal(models.Model):
	
	TYPE_PERCENT_OFF = 1
	TYPE_AMOUNT_OFF = 2
	TYPE_PERCENT_OFF_DISH = 3
	TYPE_AMOUNT_OFF_DISH = 4
	TYPE_FREE_ITEM = 5
	TYPE_CHOICES = [
		(TYPE_PERCENT_OFF, _("Percent off total")),
		(TYPE_AMOUNT_OFF, _("Amount off total")),
		(TYPE_PERCENT_OFF_DISH, _("Percent off dish")),
		(TYPE_AMOUNT_OFF_DISH, _("Amount off dish")),
		(TYPE_FREE_ITEM, _("Free item")),
	]
	
	user			= models.ForeignKey('user_profiles.UserProfile')
	restaurant		= models.ForeignKey('restaurant.Restaurant', related_name="deals")#TODO Once the restaurants field is OK, this field should be deleted
	restaurants		= models.ManyToManyField('restaurant.Restaurant')
	title			= models.CharField(max_length=200)
	type			= models.IntegerField(choices=TYPE_CHOICES)
	amount			= models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
	dish			= models.ForeignKey('dish.Dish', null=True, blank=True)
	start_datetime	= models.DateTimeField()
	end_datetime	= models.DateTimeField()
	ongoing			= models.BooleanField(default=False)
	conditions		= models.TextField(null=True, blank=True)
	cover			= models.ForeignKey('photos.Photo', null=True, blank=True)

#	def get_photo(self):
#		if self.dish:
#			return self.dish.cover_photo
#		else:
#			return self.restaurant.logo
	
	def get_time_range(self):
		#if self.ongoing:
		#	return _("Ongoing")
		if self.start_datetime and self.end_datetime:
			return _("From %s to %s" % (self.start_datetime.strftime("%m-%d-%Y"), self.end_datetime.strftime("%m-%d-%Y")))
		if self.start_datetime:
			return _("From %s" % self.start_datetime.strftime("%m-%d-%Y"))
		if self.end_datetime:
			return _("Until %s" % self.end_datetime.strftime("%m-%d-%Y"))
		return None
		
	def get_description(self):
		if self.type == self.TYPE_PERCENT_OFF:
			return "%s% off total" % self.amount
		elif self.type == self.TYPE_AMOUNT_OFF:
			return "$%s off total" % self.amount
		elif self.type == self.TYPE_PERCENT_OFF_DISH:
			return "%s %s%% off" % (self.dish.name, self.amount)
		elif self.type == self.TYPE_AMOUNT_OFF_DISH:
			return "%s $%s off" % (self.dish.name, self.amount)
		else:
			return "Free %s" % self.dish.name
		
	def get_next(self):
		next = Deal.objects.filter(id__gt=self.id)
		if next:
			return next[0]
		return False	
		
	def get_prev(self):
		prev = Deal.objects.filter(id__lt=self.id)
		if prev:
			return prev[0]
		return False

