""" Gulu ranking module models """

__author__ = "DE <denehs@gmail.com>"
__version__ = "$Id$"

from django.db import models

class BaseRankingRecord(models.Model):
    score           = models.IntegerField(default=0) 
    
    class Meta:
        abstract    = True
        ordering    = ['-score']

class DishRankingRecord(BaseRankingRecord):
    item            = models.ForeignKey('dish.Dish')
    rating          = models.IntegerField(default=0)
    comment         = models.IntegerField(default=0)
    view            = models.IntegerField(default=0)
    activity        = models.IntegerField(default=0)
    num_photo       = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.item.name
    
    def calc_score(self):
        self.score = \
            1 * self.rating + \
            1 * self.comment + \
            1 * self.view + \
            1 * self.activity + \
            1 * self.num_photo
    
