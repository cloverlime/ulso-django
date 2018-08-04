# TODO A big one!!!!

from django import forms
from django.forms import ModelForm

from ulsosite.info.info import INSTRUMENT_LIST
from ulsosite.models.concerts import (
    # PlayerPerProject,
    Rehearsal,
    Absence,
    Concert
)

# class ProjectSignUp(ModelForm):
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     instrument = forms.ChoiceField(choices=INSTRUMENT_LIST)

#     can_make_concert = forms.BooleanField(label="I can make the concert")

#     class Meta:
#         model = PlayerPerProject
#         exclude = ['project', 'musician']
