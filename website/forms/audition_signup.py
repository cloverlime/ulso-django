from django import forms
from django.forms import ModelForm

from ulsosite.models.people import Musician

class AuditionSignUpForm(ModelForm):
    title = "Audition Sign-Up"
    class Meta:
        model = Musician
        exclude = ['modified', 'status', 'subs_paid', 'alias', 'season']
