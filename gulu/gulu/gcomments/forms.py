""" Gulu comments module forms """

__author__ = "Ben Homnick <bhomnick@gmail.com>"
__version__ = "$Id: forms.py 388 2010-12-16 06:59:01Z ben $"

from django import forms
from django.contrib.comments.forms import CommentForm
from gcomments.models import GComment

class GCommentForm(CommentForm):

    def get_comment_model(self):
        return GComment

    def get_comment_create_data(self):
        data = super(GCommentForm, self).get_comment_create_data()
        return data