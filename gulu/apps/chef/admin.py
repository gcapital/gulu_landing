""" Chef admin configuration """

from django.contrib import admin

from chef.models import Chef
 
admin.site.register(Chef)
