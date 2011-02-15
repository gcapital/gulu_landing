import datetime
from django.db import models
import base64

class ReviewManager(models.Manager):
    def sid_source(self, enc_str):
        s = base64.b64decode(enc_str)
        id, created = s.split('_', 1)
        return {'id':id, 'created':created}

class Review(models.Model):
    restaurant = models.ForeignKey('restaurant.Restaurant')
    user = models.ForeignKey('user_profiles.UserProfile')
    dish = models.ForeignKey('dish.Dish', null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField()
    total_comment = models.IntegerField(default=0)
    photo = models.ForeignKey('photos.Photo', null=True, blank=True, related_name='photo_review_related')
    created = models.DateTimeField(default=datetime.datetime.now)
    def sid(self):
        return base64.b64encode("%s_%s" % (self.pk, self.created))
    objects = ReviewManager()

class ReviewHelpul(models.Model):
    review = models.ForeignKey('Review')
    user = models.ForeignKey('user_profiles.UserProfile')
    helpful_yes = models.BooleanField()
    helpful_no = models.BooleanField()
    time_stamp = models.TimeField(auto_now_add=True)
