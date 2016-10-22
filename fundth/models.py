from __future__ import unicode_literals

from django.db import models

from django.forms import ModelForm

# Create your models here.

class UserForm(ModelForm):
    # class Meta:
    #     model = User  
    pass

class UserProfileForm(ModelForm):
    # class Meta:
    #     model = UserProfile
    #     exclude = ['user']
    pass