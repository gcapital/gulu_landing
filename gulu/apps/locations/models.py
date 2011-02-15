""" Gulu locations module models

Based on django-friends written by James Tauber
<https://github.com/jtauber/django-friends>
"""

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: models.py 388 2010-12-16 06:59:01Z ben $"

import datetime

from django.db import models
from django.db.models import signals
from django.utils.translation import ugettext_lazy as _

class OtherLocationManager(models.Manager):
	
	def other_locations_for_restaurant(self, r):
		ols = []
		for ol in self.filter(from_restaurant=r).select_related(depth=1):
			ols.append({"restaurant": ol.to_restaurant, "other_location": ol})
		for ol in self.filter(to_restaurant=r).select_related(depth=1):
			ols.append({"restaurant": ol.from_restaurant, "other_location": ol})
		return ols
	
	def are_other_locations(self, r1, r2):
		if self.filter(from_restaurant=r1, to_restaurant=r2).count() > 0:
			return True
		if self.filter(from_restaurant=r2, to_restaurant=r1).count() > 0:
			return True
		return False
	
	def remove(self, r1, r2):
		if self.filter(from_restaurant=r1, to_restaurant=r2):
			ol = self.filter(from_restaurant=r1, to_restaurant=r2)
		elif self.filter(from_restaurant=r2, to_restauarant=r1):
			ol = self.filter(from_restaurant=r2, to_restaurant=r1)
		ol.delete()


class OtherLocation(models.Model):
	"""
	An other location is a relationship between two restaurants, for instance
	a restaurant and its branch location.
	"""
	
	to_restaurant = models.ForeignKey('restaurant.Restaurant', related_name="other_locations")
	from_restaurant = models.ForeignKey('restaurant.Restaurant', related_name="_unused_")
	added = models.DateField(default=datetime.date.today)
	
	objects = OtherLocationManager()
	
	class Meta:
		unique_together = (('to_restaurant', 'from_restaurant'),)

def other_locations_for(restaurant):
	return set([obj["restaurant"] for obj in OtherLocation.objects.other_locations_for_restaurant(restaurant)])


class OtherLocationInvitationManager(models.Manager):
	
	def invitations(self, *args, **kwargs):
		return self.filter(*args, **kwargs).exclude(status__in=[OtherLocationInvitation.STATUS_DELETED,])


class OtherLocationInvitation(models.Model):
	"""
	An invitation from one restaurant from another to be grouped together
	as other locations.
	"""
	
	STATUS_SENT = 1
	STATUS_ACCEPTED = 2
	STATUS_DECLINED = 3
	STATUS_DELETED = 4
	STATUS_CHOICES = (
		(STATUS_SENT, _("Sent")),
		(STATUS_ACCEPTED, _("Accepted")),
		(STATUS_DECLINED, _("Declined")),
		(STATUS_DELETED, _("Deleted")),
	)
	
	from_restaurant = models.ForeignKey('restaurant.Restaurant', related_name="invitations_from")
	to_restaurant = models.ForeignKey('restaurant.Restaurant', related_name="invitations_to")
	sent = models.DateField(default=datetime.date.today)
	status = models.IntegerField(choices=STATUS_CHOICES)
	
	objects = OtherLocationInvitationManager()
	
	def accept(self):
		if not OtherLocation.objects.are_other_locations(self.to_restaurant, self.from_restaurant):
			ol = OtherLocation(to_restaurant=self.to_restaurant, from_restaurant=self.from_restaurant)
			ol.save()
			self.status = self.STATUS_ACCEPTED
			self.save()

	def decline(self):
		if not OtherLocation.objects.are_other_locations(self.to_restaurant, self.from_restaurant):
			self.status = self.STATUS_DECLINED
			self.save()


def delete_other_location(sender, instance, **kwargs):
	ol_invitations = OtherLocationInvitation.objects.filter(to_restaurant=instance.to_restaurant, from_restaurant=instance.from_restaurant)
	for ol_invitation in ol_invitations:
		if ol_invitation.status != OtherLocationInvitation.STATUS_DELETED:
			ol_invitation.status = OtherLocationInvitation.STATUS_DELETED
			ol_invitation.save()

signals.pre_delete.connect(delete_other_location, sender=OtherLocation)