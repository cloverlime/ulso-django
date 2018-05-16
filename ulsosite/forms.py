from django import forms
from django.db import models
from django.forms import ModelForm

from ulsosite.models import Musician, ConcertoApplicant

class SignUp(ModelForm):
    class Meta:
        model = Musician
        fields = ['first_name', 'last_name', 'email', 'instrument', 'doubling', 'uni', 'other_uni', 'experience', 'returning_member']

class ConcertoForm(ModelForm):
    class Meta:
        model = ConcertoApplicant
        fields = '__all__'

class ContactForm(forms.Form):
    EMAIL_TOPIC_CHOICES = (
        ('Auditions', 'Auditions'),
        ('Late/Absent', 'Lateness/Absence'),
        ('Percussion hire', 'Percussion hire'),
        ('Conducting', 'Conducting'),
        ('Concerto', 'Concerto Competition'),
        ('Sponsorship', 'Sponsorship'),
        ('Publicity', 'Publicity'),
        ('Concert Queries', 'Concert Queries'),
        ('Subs', 'Membership and Subs'),
        ('Website', 'Website'),
        ('Other', 'Other'),
    )
    name = forms.CharField(label='Name', max_length=50)
    email = forms.EmailField(label='Your Email Address', max_length=30)
    topic = forms.ChoiceField(label='Topic', choices=EMAIL_TOPIC_CHOICES)
    subject = forms.CharField(label='Subject', max_length=150)
    message = forms.CharField(label='Message', widget=forms.Textarea, max_length=100000)
    send_self = forms.BooleanField(label="Send myself a copy", required=False)
