import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, BadHeaderError
from django.views import View
from django.urls import reverse

from ulsosite.utils import academic_year_calc
from ulsosite.models.people import ConcertoApplicant
from website.forms.concerto_signup_form import ConcertoForm


class ConcertoSignUp(View):
    season = academic_year_calc(datetime.datetime.now())

    def post(self, request, *args, **kwargs):
        form = ConcertoForm(data=request.POST)
        success_template = 'website/forms/form-success.html'
        fail_template = 'website/forms/form-fail.html'

        # create instances!
        if form.is_valid():
            data = form.cleaned_data

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
                    season=self.season
                )
                applicant.save()
            except:
                messages.add_message(request, messages.ERROR, 'There was a database error. Please report this issue immediately to webmaster@ulso.co.uk.')
                return redirect(reverse('form_error'))
                        
            messages.add_message(request, messages.SUCCESS, 'Thank you for your submission. We will get back to you soon.')
            return redirect(reverse('form_success'))

    def get(self, request, *args, **kwargs):
        form = ConcertoForm()
        form_template = 'website/pages/concerto-signup.html'

        title = "Concerto Competition"

        context = {
            'form': form,
            'title': title,
            'season': self.season,
        }
        return render(request, form_template, context)  