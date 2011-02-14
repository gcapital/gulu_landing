import datetime
import json
from haystack import indexes
from haystack import site
from user_profiles.models import UserProfile
from search.utils import Ycas
class UserProfileIndex(indexes.SearchIndex):
    text = indexes.CharField(use_template=True, document=True)
    name = indexes.CharField(model_attr='username')
    
#    def get_queryset(self):
#        return UserProfile.objects.filter(created__lte=datetime.datetime.now())
#    
#    def prepare_name(self, obj):
#        ws = json.loads(Ycas.ws(obj.name.encode('utf8')))
#        wsstr = ''
#        for o in ws:
#            wsstr+=o['token']+' '
#        return "%s" % (wsstr.rstrip())
#    
#    def prepare_description(self, obj):
#        ws = json.loads(Ycas.ws(obj.description.encode('utf8')))
#        wsstr = ''
#        for o in ws:
#            wsstr+=o['token']+' '
#        return "%s" % (wsstr.rstrip())

site.register(UserProfile, UserProfileIndex)
