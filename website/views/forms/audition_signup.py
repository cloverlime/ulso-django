import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from ulsosite.utils import academic_year_calc
from ulsosite.models.auditions import AuditionDate
from ulsosite.models.people import Musician

from website.views.forms.generic import GenericFormView
from website.forms.audition_signup import AuditionSignUpForm

class AuditionSignUpView(GenericFormView):
    form_template = 'website/pages/audition-signup.html'
    def post(self, request, *args, **kwargs):
        form = AuditionSignUpForm(data=request.POST)
        success_template = 'website/forms/form-success.html'
        success_message = "Thank you for signing up to ULSO."

        if form.is_valid():
            field_attr = form.cleaned_data
            musician = Musician.create(field_attr)

            if musician == None:
                return HttpResponse("There was an error. Please report this to webmaster@ulso.co.uk.")

            musician.save()

            # TODO Send acknowledgement email

            context = {'message': success_message }
            return render(request, success_template , context)
        
        else:
            # Render tempalte again with error messages
            
            context = {
            'form': form,
            'season': season,
            'audition_dates': audition_dates
        }
            return render(request, self.form_template, context)

        return HttpResponse("oops something went wrong")

    def get(self, request, *args, **kwargs):
        form = AuditionSignUpForm()
        form_title = "Audition Sign-Up"
        season = academic_year_calc(datetime.datetime.now())

        # Queryset of audition dates for the current season
        audition_dates = AuditionDate.objects.filter(season=season)
        context = {
            'form': form,
            'season': season,
            'audition_dates': audition_dates
        }
        return render(request, self.form_template, context)
