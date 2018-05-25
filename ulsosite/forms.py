from django import forms
from django.db import models
from django.forms import ModelForm

from ulso_admin.models import Musician, ConcertoApplicant

# class SignUp(ModelForm):
#     title = "Audition Sign-Up"
#     class Meta:
#         model = AuditionApplicant
#         exclude = ['status', 'subs_paid', 'alias', 'season']


class ConcertoForm(ModelForm):
    title = "Concerto Competition Sign-Up"
    class Meta:
        model = ConcertoApplicant
        exclude = ['alias', 'second_round']

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
