from django import forms
from django.forms import ModelForm

from ulsosite.info.info import INSTRUMENT_LIST
from ulsosite.models.concerts import (
    Rehearsal,
    Absence,
    Concert
)

class ProjectSignUp(forms.Form):

    def get_current_rehearsals():
        return Rehearsal.objects.filter(
            concert=Concert.objects.filter(current=True).first()
            ).order_by('date')

    first_name = forms.CharField(max_length=50, help_text="As registered")
    last_name = forms.CharField(max_length=50, help_text="As registered")
    email = forms.EmailField(
        label="Email", 
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'example@email.com'}),
        help_text="As registered"
    )
    PROJECT_CHOICES = (
        ('Yes', 'Yes, I will play in this project'),
        ('No', 'No, I can\'t play this time'),
    )
    instrument = forms.ChoiceField(choices=INSTRUMENT_LIST, help_text="Select your main instrument")
    can_make_concert = forms.ChoiceField(choices=PROJECT_CHOICES)
    attendance = forms.ModelMultipleChoiceField(
        queryset=get_current_rehearsals(),
        widget=forms.widgets.CheckboxSelectMultiple(
            attrs={
                'class': 'attendance-choices'
            }
        ),
        help_text="Please tick ALL the rehearsals that you CAN make. Deps are mandatory for wind, brass, percussion and string leaders. Attendance is compulsory for everyone on the day of the concert."
    )