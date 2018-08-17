import datetime
import pprint as pp
from django.shortcuts import render
from django.core.mail import EmailMessage, BadHeaderError
from django.views import View

from ulsosite.utils import academic_year_calc
from ulsosite.models.people import ConcertoApplicant
from website.forms.concerto_signup_form import ConcertoForm

class ConcertoSignUp(View):
    def post(self, request, *args, **kwargs):
        form = ConcertoForm(data=request.POST)
        success_template = 'website/forms/form-success.html'
        fail_template = 'website/forms/form-fail.html'

        # create instances!
        if form.is_valid():
            data = form.cleaned_data
            pp.pprint(data)

            try:
                applicant = ConcertoApplicant.objects.create(
                    first_name=data['first_name'], 
                    last_name=data['last_name'],
                    email=data['email'],
                    phone=data['phone'],
                    instrument=data['instrument'],
                    piece=data['piece'],
                    years_ulso_member=data['years_ulso_member'],
                    notes=data['notes'],
                )
                print(applicant)
                applicant.save()
            except Exception as e:
                print(e)
                return render(request, fail_template, { 
                    'message': 'There was an error. Please report to webmaster@ulso.co.uk.'}
                    )
            
            context = { 'message': 'Thank you for your submission.'}
            return render(request, success_template, context) 

    def get(self, request, *args, **kwargs):
        form = ConcertoForm()
        form_template = 'website/pages/concerto-signup.html'

        title = "Concerto Competition"
        season = academic_year_calc(datetime.datetime.now())

        context = {
            'form': form,
            'title': title,
            'season': season,
        }
        return render(request, form_template, context)  