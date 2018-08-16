from django import forms
from ulsosite.models.concerts import Concert, Rehearsal

class AbsenceForm(forms.Form):
    # rehearsal_set = Rehearsal.objects.filter(
    #     concert=Concert.objects.get(current=True)
    # )
    rehearsal = forms.ModelChoiceField(
        label="Rehearsal",
        queryset=Rehearsal.objects.filter(
        concert=Concert.objects.get(current=True)
    ),
        widget=forms.Select
    )
    full_name = forms.CharField(max_length=20, help_text="As registered")
    email = forms.EmailField(label="Your email address", max_length=100, help_text="As registered")
    instrument = forms.CharField(max_length=20, help_text="For this particular project")
    dep_name = forms.CharField(label="Deputy's Full Name", max_length=20, required=False, help_text="A dep is mandatory for wind, brass, percussion and string leaders.")
    dep_email = forms.EmailField(label="Dep's email address", required=False, max_length=100, help_text="This is for us to notify your dep about our privacy policy, and gives them information on how to contact us if need be. They will also be sent our privacy policy.")
    dep_phone = forms.CharField(max_length=20, required=False, help_text="Please give us your dep's phone number if at all possible. We will only contact them in the case of unexpected events to do with the rehearsal.")
    reasons = forms.CharField(max_length=200, widget=forms.Textarea(
        attrs={
                'placeholder': 'Your answer',
                'rows':'4',
                'cols':'40',
            }
        ),
    )