import datetime
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey

class Todo(models.Model):

	# Generic association
	content_type 	= models.ForeignKey(ContentType, null=True, blank=True)
	object_id 		= models.PositiveIntegerField(null=True, blank=True)
	content_object 	= GenericForeignKey()    
