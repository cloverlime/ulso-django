import datetime
from django import forms

from ulsosite.utils import academic_year_calc
from ulsosite.info.info import (
    INSTRUMENT_LIST,
    UNI_LIST,
    YEAR_LIST
)


class AuditionSignUpForm(forms.Form):
    season = academic_year_calc(datetime.datetime.now())
    title = f"Audition Sign-Up {season}"

    # Name and contact details
    first_name = forms.CharField(
        label="First name",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your first name',
                'autofocus': 'autofocus'
            }
        )
    )
    last_name = forms.CharField(
        label="Last name",
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Your last name'})
        )
    email = forms.EmailField(
        label="Email", 
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'example@email.com'}),
        help_text="Please enter your preferred email address"
        )
    phone = forms.CharField(
        label="Mobile Number",
        widget=forms.TextInput(attrs={'placeholder': '01234 567890'}),
        max_length=15,
        help_text="Having your number is very helpful for us in the case of unforeseen circumstances."
        )
    
    # Uni status
    uni = forms.ChoiceField(label="College or University", choices=UNI_LIST)
    other_uni = forms.CharField(
        label="Other",
        max_length=50,
        required=False,
        help_text="If you selected 'Other', please enter your university here"
    )
    year = forms.ChoiceField(label="Year of course", choices=YEAR_LIST)
    
    # Instrument and experience
    returning_member = forms.BooleanField(
        label="Returning member",
        required=False,
        help_text="Are you a returning member of ULSO?"
    )
    instrument = forms.ChoiceField(
        label="Instrument",
        choices=INSTRUMENT_LIST,
        help_text="Please select your main instrument here. If you play the harp, piano or saxophone, you will be considered for addition to ULSO's extras list for this season and may be invited to play depending on the repertoire.")
    doubling = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. piccolo, Eb clarinet, cor anglais...'}),
        help_text="Please list any doubling or additional instruments you wish to be considered on."
    )    
    experience = forms.CharField(
        max_length=300,
        widget=forms.Textarea(
            attrs={
                'rows':'4',
                'cols':'40',
                }
            ),
        help_text="Please give a brief list of your recent orchestral experience."
    )
    
    # Agreements
    depping_policy = forms.BooleanField(required=True, help_text='Tick here to agree to abide to our depping policy.')
    privacy_policy = forms.BooleanField(required=True, help_text='Tick here to indicate that you have read and agreed to our privacy policy.')

    # Other
    notes = forms.CharField(
        max_length=500,
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Your answer',
            'rows':'4',
            'cols':'40',
            }),
        help_text="If you are unable to make any of the dates above, please let us know when you might be available. Also add any other preferences or comments below."
        )
    