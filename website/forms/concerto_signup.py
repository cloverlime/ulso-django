from django import forms
from ulsosite.models.people import ConcertoApplicant

class ConcertoForm(ModelForm):
    title = "Concerto Competition Sign-Up"
    class Meta:
        model = ConcertoApplicant
        exclude = ['created', 'modified','alias', 'second_round']
