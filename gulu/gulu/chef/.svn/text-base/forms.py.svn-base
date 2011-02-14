""" Gulu chef module forms """

from django import forms
from chef.models import Chef

class AddEditChefForm(forms.ModelForm):
    """ Form used for adding and editing deals """
    
    class Meta:
        model = Chef
        fields = (
            'name',
            'description',
            'points',
        )