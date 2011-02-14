from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, require_mime, require_extended

from dish.models import Dish
from review.models import Review
from deal.models import Deal
from restaurant.models import Restaurant
from user_profiles.models import UserProfile
from event.models import Event
from photos.models import Photo
from wall.models import WallPost
from wall.forms import WallPostForm
from gcomments.models import GComment
from actstream import action
from actstream.models import Action
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseBadRequest
import time
from datetime import datetime

PTEST = False
IMAGE_LARGE = 'image600x400'
IMAGE_MEDIUM = 'image185x185'
IMAGE_SMALL = 'image50x50'

WALL_TYPE = ContentType.objects.get_for_model(WallPost)
USERPROFILE_TYPE = ContentType.objects.get_for_model(UserProfile)
ACTION_TYPE = ContentType.objects.get_for_model(Action)

# GET objects


"""Need modified for MongoDB"""
class get_wall_post_by_uid(BaseHandler):
    #fields=('id','poster','content','created','comment_count','time_ago')
    #fields=('action_object_object_id',)      
    def read (self, request):
        uid = request.GET.get('uid')
        if PTEST:
            uid = 4                
        action_list = Action.objects.filter(actor_content_type=USERPROFILE_TYPE, actor_object_id=uid, action_object_content_type=WALL_TYPE)
        ret = []
        for a in action_list:
            wall_o = a.action_object
            comment_list = GComment.objects.filter(content_type=ACTION_TYPE,object_pk=a.id)
            num = len(comment_list)
            unix_seconds = time.mktime(datetime.now().timetuple()) - time.mktime(wall_o.created.timetuple())
            wall_dict = {'id':wall_o.id,'poster':wall_o.poster,'content':wall_o.content,
                         'created':wall_o.created, 'comment_count':num, 'time_ago':unix_seconds}
            ret.append(wall_dict)
        ret.reverse() #Let the most Recently on top
        return ret
    
    def create (self, request):
        uid = request.POST.get('uid')
        if PTEST:
            uid = 4                
        action_list = Action.objects.filter(actor_content_type=USERPROFILE_TYPE, actor_object_id=uid, action_object_content_type=WALL_TYPE)
        ret = []
        for a in action_list:
            wall_o = a.action_object
            comment_list = GComment.objects.filter(content_type=ACTION_TYPE,object_pk=a.id)
            num = len(comment_list)
            unix_seconds = time.mktime(datetime.now().timetuple()) - time.mktime(wall_o.created.timetuple())
            wall_dict = {'id':wall_o.id,'poster':wall_o.poster,'content':wall_o.content,
                         'created':wall_o.created, 'comment_count':num, 'time_ago':unix_seconds}
            ret.append(wall_dict)
        ret.reverse() #Let the most Recently on top
        return ret

"""Need Define Input"""
class create_wall_post(BaseHandler):
    def read (self, request):        
        uid = request.GET.get('uid')
        content = request.GET.get('text')
        if PTEST:
            uid = 4
        if not content:
            content = "First test(by app)"
        user=get_object_or_404(UserProfile, id=uid)        
        wall_o = WallPost(poster=user,content=content,owner_content_type=USERPROFILE_TYPE,owner_object_id=uid)
        wall_o.save()
        action.send(user,verb='posted on',action_object=wall_o,target=wall_o)
        wall_dict = {'id':wall_o.id,'poster':wall_o.poster,'content':wall_o.content,
                     'created':wall_o.created, 'comment_count':0, 'time_ago':0}
        #gc_o = GComment(commenter=user,comment='mycomment',content_type=WALL_TYPE,object_pk=4,user=user,submit_date=datetime.now(),site_id=1)
        #gc_o.save()
        return wall_dict
    def create (self, request):        
        uid = request.POST.get('uid')
        content = request.POST.get('text')
        if PTEST:
            uid = 4
        if not content:
            content = "First test(by app)"
        user=get_object_or_404(UserProfile, id=uid)        
        wall_o = WallPost(poster=user,content=content,owner_content_type=USERPROFILE_TYPE,owner_object_id=uid)
        wall_o.save()
        action.send(user,verb='posted on',action_object=wall_o,target=wall_o)
        wall_dict = {'id':wall_o.id,'poster':wall_o.poster,'content':wall_o.content,
                     'created':wall_o.created, 'comment_count':0, 'time_ago':0}
        #gc_o = GComment(commenter=user,comment='mycomment',content_type=WALL_TYPE,object_pk=4,user=user,submit_date=datetime.now(),site_id=1)
        #gc_o.save()
        return wall_dict

"""Watch out the SITEID!!!!!"""
class create_wall_post_comment(BaseHandler):
    def read (self, request):        
        content = request.GET.get('text')
        pid = request.GET.get('pid')
        uid = request.GET.get('uid')
        if not pid:
            pid = 16
        if not content:
            content = "Comment test(by app)"
        if PTEST:
            uid = 3
        wall_o = get_object_or_404(WallPost, id=pid)
        #action_o = Action.objects.get(action_object_content_type=WALL_TYPE,action_object_object_id=pid)
        action_o = get_object_or_404(Action,action_object_content_type=WALL_TYPE,action_object_object_id=pid)
        aid = action_o.id
        user = get_object_or_404(UserProfile, id=uid)
        if user.first_name or user.last_name:
            user_name=user.get_full_name()
        else:
            user_name=user.username
        gc_o = GComment(commenter=user,comment=content,content_type=ACTION_TYPE,
                        object_pk=aid,user=user,submit_date=datetime.now(),site_id=1,user_name=user_name)
        gc_o.save()
        gc_dict = {'id':gc_o.id,'user':gc_o.commenter,'content':gc_o.comment,
                   'created':gc_o.submit_date, 'time_ago':0, 'post_id':pid}
        return gc_dict
    def create (self, request):        
        content = request.POST.get('text')
        pid = request.POST.get('pid')
        uid = request.POST.get('uid')
        if not pid:
            pid = 16
        if not content:
            content = "Comment test(by app)"
        if PTEST:
            uid = 3
        wall_o = get_object_or_404(WallPost, id=pid)
        #action_o = Action.objects.get(action_object_content_type=WALL_TYPE,action_object_object_id=pid)
        action_o = get_object_or_404(Action,action_object_content_type=WALL_TYPE,action_object_object_id=pid)        
        aid = action_o.id
        user = get_object_or_404(UserProfile, id=uid)
        if user.first_name or user.last_name:
            user_name=user.get_full_name()
        else:
            user_name=user.username
        gc_o = GComment(commenter=user,comment=content,content_type=ACTION_TYPE,
                        object_pk=aid,user=user,submit_date=datetime.now(),site_id=1,user_name=user_name)
        gc_o.save()
        gc_dict = {'id':gc_o.id,'user':gc_o.commenter,'content':gc_o.comment,
                   'created':gc_o.submit_date, 'time_ago':0, 'post_id':pid}
        return gc_dict
    
class get_wall_comment_by_postid(BaseHandler):
    def read (self, request):        
        pid = request.GET.get('pid')
        if not pid:
            pid = 16
        #action_o = Action.objects.get(action_object_content_type=WALL_TYPE,action_object_object_id=pid)
        action_o = get_object_or_404(Action,action_object_content_type=WALL_TYPE,action_object_object_id=pid)
        aid = action_o.id
        gc_list = GComment.objects.filter(content_type=ACTION_TYPE,object_pk=aid)
        ret = []
        for gc_o in gc_list:
            unix_seconds = time.mktime(datetime.now().timetuple()) - time.mktime(gc_o.submit_date.timetuple())
            gc_dict = {'id':gc_o.id,'user':gc_o.commenter,'content':gc_o.comment,
                   'created':gc_o.submit_date, 'time_ago':unix_seconds, 'post_id':pid}
            ret.append(gc_dict)
        return ret
    def create (self, request):        
        pid = request.POST.get('pid')
        if not pid:
            pid = 16
        #action_o = Action.objects.get(action_object_content_type=WALL_TYPE,action_object_object_id=pid)
        action_o = get_object_or_404(Action,action_object_content_type=WALL_TYPE,action_object_object_id=pid)
        aid = action_o.id
        gc_list = GComment.objects.filter(content_type=ACTION_TYPE,object_pk=aid)
        ret = []
        for gc_o in gc_list:
            unix_seconds = time.mktime(datetime.now().timetuple()) - time.mktime(gc_o.submit_date.timetuple())
            gc_dict = {'id':gc_o.id,'user':gc_o.commenter,'content':gc_o.comment,
                   'created':gc_o.submit_date, 'time_ago':unix_seconds, 'post_id':pid}
            ret.append(gc_dict)
        return ret


"""Need Modify user auth issue and return protocol"""
"""Need Modify uid from integer to string"""
class delete_wall_post(BaseHandler):
    def read (self, request):        
        pid = request.GET.get('pid')
        uid = request.GET.get('uid')
        #action_o = Action.objects.get(action_object_content_type=WALL_TYPE,action_object_object_id=pid)        
        action_o = get_object_or_404(Action,action_object_content_type=WALL_TYPE,action_object_object_id=pid)
        if action_o.actor_object_id != int(uid):
            return HttpResponseBadRequest({ 'errorMessage':1 })
        aid = action_o.id
        action_o.delete()
        wall_o = get_object_or_404(WallPost, id=pid)
        wall_o.delete()        
        gc_list = GComment.objects.filter(content_type=ACTION_TYPE,object_pk=aid)
        for gc_o in gc_list:
            gc_o.delete()
        return { 'errorMessage':0 }
    
    def create (self, request):        
        pid = request.POST.get('pid')
        uid = request.POST.get('uid')
        #action_o = Action.objects.get(action_object_content_type=WALL_TYPE,action_object_object_id=pid)        
        action_o = get_object_or_404(Action,action_object_content_type=WALL_TYPE,action_object_object_id=pid)
        if action_o.actor_object_id != int(uid):
            return HttpResponseBadRequest({ 'errorMessage':1 })
        aid = action_o.id
        action_o.delete()
        wall_o = get_object_or_404(WallPost, id=pid)
        wall_o.delete()        
        gc_list = GComment.objects.filter(content_type=ACTION_TYPE,object_pk=aid)
        for gc_o in gc_list:
            gc_o.delete()
        return { 'errorMessage':0 }
    
class delete_wall_post_comment(BaseHandler):
    def read (self, request):        
        cid = request.GET.get('cid')
        uid = request.GET.get('uid')
        gc_o = get_object_or_404(GComment, id=cid)
        if gc_o.commenter.id != int(uid):
            return HttpResponseBadRequest({ 'errorMessage':1 })            
        gc_o.delete()
        return { 'errorMessage':0 }
    def create (self, request):        
        cid = request.POST.get('cid')
        uid = request.POST.get('uid')
        gc_o = get_object_or_404(GComment, id=cid)
        if gc_o.commenter.id != int(uid):
            return HttpResponseBadRequest({ 'errorMessage':1 })            
        gc_o.delete()
        return { 'errorMessage':0 }
