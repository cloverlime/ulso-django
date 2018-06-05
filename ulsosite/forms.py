from django import forms
from django.forms import ModelForm

from ulsosite.info.info import INSTRUMENT_LIST
from ulsosite.models.concerts import PlayerPerProject
from ulsosite.models.people import (
                                Musician,
                                ConcertoApplicant,
                                                    )


class AuditionSignUp(ModelForm):
    title = "Audition Sign-Up"
    class Meta:
        model = Musician
        exclude = ['modified', 'status', 'subs_paid', 'alias']

class ConcertoForm(ModelForm):
    title = "Concerto Competition Sign-Up"
    class Meta:
        model = ConcertoApplicant
        exclude = ['created', 'modified','alias', 'second_round']

class ProjectSignUp(ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    instrument = forms.ChoiceField(choices=INSTRUMENT_LIST)

    can_make_concert = forms.BooleanField(label="I can make the concert")

    class Meta:
        model = PlayerPerProject
        exclude = ['project', 'musician']

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
