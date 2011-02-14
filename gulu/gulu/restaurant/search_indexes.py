import datetime
import json
from haystack import indexes
from haystack import site
from restaurant.models import Restaurant
from search.utils import Ycas
class RestaurantIndex(indexes.SearchIndex):
    text = indexes.CharField(use_template=True, document=True)
    name = indexes.CharField(model_attr='name')
#    address = indexes.CharField(model_attr='address')
#    description = indexes.CharField(model_attr='description')
    
    def get_queryset(self):
        return Restaurant.objects.filter(created__lte=datetime.datetime.now())
    
    # to see the data build to index, you can comment this function
    def prepare(self, obj):
        self.prepared_data = super(RestaurantIndex, self).prepare(obj)
        print "=========INDEX START==========="
        print self.prepared_data
        print "=========INDEX END============="
        return self.prepared_data
    
    # Using Yahoo Segmentation API before indexing a field
    def prepare_text(self, obj):
        ws = json.loads(Ycas.ws(obj.name.encode('utf8')))
        wsstr = ''
        for o in ws:
            wsstr+=o['token']+' '
        print wsstr
        return "%s" % (wsstr.rstrip())
    
#    def prepare_description(self, obj):
#        ws = json.loads(Ycas.ws(obj.description.encode('utf8')))
#        wsstr = ''
#        for o in ws:
#            wsstr+=o['token']+' '
#        return "%s" % (wsstr.rstrip())

site.register(Restaurant, RestaurantIndex)
