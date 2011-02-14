""" Like tests """

from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
from django.template import Context, Template
from django.test import TestCase
from django.test.client import Client

from like.models import Like, user_model
from user_profiles.models import UserProfile

class TestModel(models.Model):
	name = models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.name

class ApiTest(TestCase):
	def setUp(self):
		self.u1 = UserProfile.objects.create(username="test")
		self.o1 = TestModel.objects.create(name="obj1")
		self.o2 = TestModel.objects.create(name="obj2")
		self.l1 = Like.objects.create(user=self.u1, content_object=self.o1)
		self.c = ContentType.objects.get_for_model(TestModel)
	
	def test_does_like(self):
		self.assertEquals(True, Like.objects.does_like(self.u1, self.o1))
		self.assertEquals(False, Like.objects.does_like(self.u1, self.o2))
		
	def test_like_unlike(self):
		Like.objects.like(self.u1, self.o2)
		self.assertEquals(True, Like.objects.does_like(self.u1, self.o2))
		Like.objects.like(self.u1, self.o2)
		self.assertEquals(True, Like.objects.does_like(self.u1, self.o2))
		self.assertEquals(1, Like.objects.filter(user=self.u1, content_type=self.c, object_id=self.o2.pk).count())
		Like.objects.unlike(self.u1, self.o2)
		self.assertEquals(False, Like.objects.does_like(self.u1, self.o2))
		Like.objects.unlike(self.u1, self.o2)
		self.assertEquals(False, Like.objects.does_like(self.u1, self.o2))
		Like.objects.unlike(self.u1, self.o1)
		self.assertEquals(set([]), Like.objects.liked_objects_for(self.u1))
		Like.objects.like(self.u1, self.o1)
		Like.objects.like(self.u1, self.o2)
		self.assertEquals(set([self.o1, self.o2]), Like.objects.liked_objects_for(self.u1))


class TagsTest(TestCase):
	def setUp(self):
		self.o1 = TestModel.objects.create(name="obj1")
		self.c = ContentType.objects.get_for_model(TestModel)
		self.get_url = lambda a, cid, oid: reverse(
			'like.views.process',
			args=(a, cid, oid),
		)
	
	def get_template(self, args):
		return "{%% load like %%}{%% get_like_process_url %s %%}" % args
		
	def test_like(self):
		url = self.get_url("like", self.c.id, self.o1.pk)
		t = Template(self.get_template('"like" obj'))
		c = Context({
			'obj': self.o1,
		})
		self.failUnlessEqual(url, t.render(c))
		
	def test_dislike(self):
		url = self.get_url("unlike", self.c.id, self.o1.pk)
		t = Template(self.get_template('"unlike" obj'))
		c = Context({
			'obj': self.o1,
		})
		self.failUnlessEqual(url, t.render(c))
	

class ViewsTest(TestCase):
	def setUp(self):
		self.u1 = UserProfile.objects.create_user(username="more", email="test@test.com", password="cowbell")
		self.o1 = TestModel.objects.create(name="obj1")
		self.c = ContentType.objects.get_for_model(TestModel)
		self.client = Client()
		self.get_url = lambda a, cid, oid: reverse(
			'like.views.process',
			args=(a, cid, oid),
		)

	def test_like_dislike(self):
		self.client.login(username="more", password="cowbell")
		
		response = self.client.get(self.get_url("like", self.c.id, self.o1.pk))
		self.failUnlessEqual(response.status_code, 200)
		self.assertEquals(True, Like.objects.does_like(self.u1, self.o1))
		
		response = self.client.get(self.get_url("unlike", self.c.id, self.o1.pk))
		self.failUnlessEqual(response.status_code, 200)
		self.assertEquals(False, Like.objects.does_like(self.u1, self.o1))

		response = self.client.get(self.get_url("like", self.c.id, self.o1.pk + 1))
		self.failUnlessEqual(response.status_code, 404)
		
		response = self.client.get(self.get_url("like", self.c.id + 9999, self.o1.pk))
		self.failUnlessEqual(response.status_code, 404)
	
		response = self.client.get("%s?next=%s" % (self.get_url("like", self.c.id, self.o1.pk), "/"))
		self.failUnlessEqual(response.status_code, 302)
		
		# AJAX test
		response = self.client.get("%s?next=%s" % (self.get_url("like", self.c.id, self.o1.pk), "/"), 
								   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
		self.failUnlessEqual(response.status_code, 200)
