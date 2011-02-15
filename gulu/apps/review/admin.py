from django.contrib import admin
from review.models import Review

class ReviewAdmin(admin.ModelAdmin):
    """ Review admin class """
    list_display = ('restaurant', 'user', 'dish', 'content', 'created')
    list_filter = ['created']
    list_per_page = 10
    
admin.site.register(Review, ReviewAdmin)