""" Gulu wall module template tags """

__author__="Ben Homnick <bhomnick@gmail.com>"
__versions__="$Id: gcomments_tags.py 388 2010-12-16 06:59:01Z ben $"

from django.template import Library

register=Library()

@register.inclusion_tag( 'inc_wall_comment.html' )
def wall_list( wall ):
    return {'wall': wall}
