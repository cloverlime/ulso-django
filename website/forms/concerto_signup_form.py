from django import forms
import datetime
from ulsosite.models.people import ConcertoApplicant
from ulsosite.info.info import INSTRUMENT_LIST

class ConcertoForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(max_length=30, help_text="Please give us your mobile nummber so we can contact you during unforeseen circumstances.")
    instrument = forms.ChoiceField(choices=INSTRUMENT_LIST)
    piece = forms.CharField(max_length=100, help_text="Please enter the piece you wish to play. This can be the same as or different from the piece you would eventually perform with ULSO.")
    years_ulso_member = forms.CharField(max_length=50, help_text="e.g. 2015-17")
    notes = forms.CharField(
        max_length=300,
        required=False,
        widget=forms.Textarea(attrs={
            'rows':'4',
            'cols':'40',
            }),
        help_text="Let us know you have any other questions, comments or requirements.")