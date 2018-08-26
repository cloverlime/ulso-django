import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from django.views import View
from django.urls import reverse

from ulsosite.utils import academic_year_calc
from ulsosite.models.auditions import AuditionDate
from ulsosite.models.people import Musician
from ulsosite.info.dates import CURRENT_SEASON

from website.forms.audition_signup import AuditionSignUpForm

from status.models import Status

class AuditionSignUpView(View):

    form_template = 'website/pages/audition-signup.html'
    fail_template = 'website/forms/form-fail.html'

    def _concerto_is_open():
        return Status.objects.get(season=CURRENT_SEASON).concerto_open

    def post(self, request, *args, **kwargs):
        form = AuditionSignUpForm(data=request.POST)
        success_template = 'website/forms/form-success.html'
        success_message = "Thank you for signing up to ULSO."
        form_error_message = 'Sorry, your form was invalid. Please try again.'

        if not self._concerto_is_open:
            context = {'message': 'We are currently closed for audition applications. Please contact us to discuss mid-year opportunities.' }
            return render(request, self.fail_template , context)
        
        if form.is_valid():
            field_attr = form.cleaned_data
            musician = Musician.create(field_attr)

            if musician == None:
                return HttpResponse("There was an error. Please report this to webmaster@ulso.co.uk.")

            musician.save()

            # TODO Send acknowledgement email

            messages.add_message(request, messages.SUCCESS, success_message)
            return redirect(reverse('form_success'))
        else:
            messages.add_message(request, messages.ERROR, form_error_message)
            return redirect(reverse('form_error'))

    def get(self, request, *args, **kwargs):
        form = AuditionSignUpForm()
        form_title = "Audition Sign-Up"
        season = academic_year_calc(datetime.datetime.now())

        if not self._concerto_is_open:
            context = {'message': 'We are currently closed for audition applications. Please contact us to discuss mid-year opportunities.' }
            return render(request, self.fail_template , context)

        # Queryset of audition dates for the current season
        audition_dates = AuditionDate.objects.filter(season=season)
        context = {
            'form': form,
            'season': season,
            'audition_dates': audition_dates
        }
        return render(request, self.form_template, context)
