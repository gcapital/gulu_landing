""" Gulu photo models """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: models.py 611 2011-01-27 09:23:09Z ben $"

import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey

from imagekit.models import ImageModel
from imagekit.lib import Image

from globals.utils import slugreverse

class PhotoManager(models.Manager):
	pass

class BasePhoto(ImageModel):
	""" Abstract photo base class """
	
	# Generic association
	content_type 	= models.ForeignKey(ContentType, null=True, blank=True)
	object_id 		= models.PositiveIntegerField(null=True, blank=True)
	content_object 	= GenericForeignKey()
	
	restaurant_id 	= models.PositiveIntegerField(null=True, blank=True)
	image 			= models.ImageField(upload_to='photos')
	title 			= models.CharField(max_length=255, null=True, blank=True)
	description 	= models.TextField(null=True, blank=True)
	view_count 		= models.PositiveIntegerField(default=0, editable=False)
	is_main 		= models.BooleanField(default=False)
	is_featured 	= models.BooleanField(default=False)
	order 			= models.IntegerField(default=0)
	user 			= models.ForeignKey('user_profiles.UserProfile', null=True, blank=True)
	created 		= models.DateTimeField(default=datetime.datetime.now)
	
	objects 		= PhotoManager()
	
	def __unicode__(self):
		return '%s %s %s' % (self.pk, self.title, self.content_object)
	
	class Meta:
		abstract = True
		ordering = ['content_type', 'object_id', 'order']
		get_latest_by = 'created'
		verbose_name = _("photo")
		verbose_name_plural = _("photos")
		
	class IKOptions:
		spec_module = "photos.imagespecs"
		save_count_as = 'view_count'
		cache_dir = 'photo_cache'
		cache_filename_format = "%(specname)s/%(filename)s.%(extension)s"

	def next(self):
		""" Returns the next image for the same content_object or None if this
		is the last image. """
		
		try:
			return self.__class__.objects.for_model(self.content_object,
				self.content_type).filter(order__lt=self.order).order_by('order')[0]
				
		except IndexError:
			return None
				
	def previous(self):
		""" Returns the previous image for the same content_object or None if this
		is the first image. """
		
		try:
			return self.__class__.objects.for_model(self.content_object,
				self.content_type).filter(order__gt=self.order).order_by('order')[0]
			
		except IndexError:
			return None

	def attach(self, obj):
		""" Attaches this photo to obj, updates content_type and object_id """
		
		self.content_type = ContentType.objects.get_for_model(obj)
		self.object_id = obj.id
		self.save()

	"""def get_absolute_url(self):
		args = [self.object_id, self.pk]
		content_object = self.content_object
		
		# Make an exception when the attached item is a Dish, since this 
		# is sort of a sub-object of Restaurant URL-wise, but not really.
		# TODO: eliminate exception
		if self.content_type == dish_type:
			args.insert(0, self.content_object.restaurant.pk)
			content_object = self.content_object.restaurant
		
		return slugreverse(content_object, 
			"photos-%s-view" % self.content_type.model,	
			args=args)
	"""
	
class Photo(BasePhoto):
	""" Non-abstract version of the BasePhoto class """

	def save(self, *args, **kwargs):
		if self.is_main:
			related_images = self.__class__.objects.filter(
				content_type = self.content_type, 
				object_id = self.object_id,
			)
			related_images.update(is_main = False)
	
		super(BasePhoto, self).save(*args, **kwargs)
