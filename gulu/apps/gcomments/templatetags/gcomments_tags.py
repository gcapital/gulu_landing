""" Gulu comments module template tags """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__versions__ = "$Id: gcomments_tags.py 388 2010-12-16 06:59:01Z ben $"

from django.template import Library

register = Library()

@register.inclusion_tag('inc_gcomments_form.html')
def comments_form(obj):
    return {'obj': obj}
