""" Wall tests """

from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
from django.test import TestCase
from django.test.client import Client
from django.utils import simplejson

from user_profiles.models import UserProfile

class TestModel(models.Model):
	name = models.CharField(max_length=20)

class WallTest(TestCase):
	def setUp(self):
		self.u = UserProfile.objects.create_user(username="more", email="test@test.com", password="cowbell")
		self.client = Client()
		self.obj = TestModel.objects.create(name="obj")
		self.ctype = ContentType.objects.get_for_model(TestModel)
		self.post_url = reverse('wall-post')
	
	def test_good_post(self):	
		self.client.login(username="more", password="cowbell")
		data = {
			'content': "post",
			'owner_content_type': self.ctype.pk,
			'owner_object_id': self.obj.pk,
		}
		response = self.client.post(self.post_url, data)
		self.failUnlessEqual(response.status_code, 200)
		self.assertEqual(simplejson.loads(response.content)['status'], 0)
	
	
	def test_anonymouse_post(self):
		# not allowed
		data = {
			'content': "post",
			'owner_content_type': self.ctype.pk,
			'owner_object_id': self.obj.pk,
		}
		response = self.client.post(self.post_url, data)
		self.failUnlessEqual(response.status_code, 302)

	
	def test_bad_post(self):
		self.client.login(username="more", password="cowbell")
		data = {
			'content': "",
			'owner_content_type': self.ctype.pk,
			'owner_object_id': self.obj.pk,
		}
		response = self.client.post(self.post_url, data)
		self.failUnlessEqual(response.status_code, 200)
		self.assertEqual(simplejson.loads(response.content)['status'], 1)
