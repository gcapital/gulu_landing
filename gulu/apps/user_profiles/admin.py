""" User profiles admin configuration """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: admin.py 576 2011-01-26 08:16:00Z ben $"

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from user_profiles.models import UserProfile

class UserProfileAdmin(UserAdmin):
	""" Custom UserAdmin class
	
	Overrides the fieldsets in the built-in UserAdmin model to allow
	support for additional fields in our custom UserProfile model.
	"""
	def __init__(self,*args,**kwargs):
		super(UserProfileAdmin,self).__init__(*args,**kwargs)
		fields = list(UserAdmin.fieldsets[1][1]['fields'])
		
		# Append any extra fields here
		fields.append('slug')
		fields.append('birthday')
		fields.append('gender')
		fields.append('profile_pics')
		fields.append('main_profile_pic')
		fields.append('nickname')
		fields.append('about_me')
		fields.append('favorite_count')
		fields.append('follower_count')
		fields.append('following_count')
		fields.append('gulu_points')
		
		UserAdmin.fieldsets[1][1]['fields']=fields

# Unregister the old User admin
admin.site.unregister(User)

# Register our shiny new admin class
admin.site.register(UserProfile, UserProfileAdmin)
