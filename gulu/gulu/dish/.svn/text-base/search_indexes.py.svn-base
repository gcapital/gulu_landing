import datetime
import json

from haystack import indexes
from haystack import site

from dish.models import Dish

class DishIndex(indexes.SearchIndex):
    text = indexes.CharField(use_template=True, document=True)
    name = indexes.CharField(model_attr='name')
    description = indexes.CharField(model_attr='description')

site.register(Dish, DishIndex)
