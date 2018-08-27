import datetime
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from ulsosite.models.concerts import Absence

from website.forms.absence import AbsenceForm
from website.utils import redirect_error, redirect_success
from website import responses

class AbsenceFormView(View):
    form_template = 'website/pages/absence-signup.html'
    success_template = 'website/forms/form-success.html'

    def get(self, request, *args, **kwargs):
        form = AbsenceForm()
        title = 'Absence'
        context = {
            'form': form,
            'title': title
        }
        return render(request, self.form_template, context)

    def post(self, request, *args, **kwargs):
        form = AbsenceForm(data=request.POST)

        # Clean the form data
        if form.is_valid():
            rehearsal = form.cleaned_data['rehearsal']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            instrument = form.cleaned_data['instrument']
            dep_name = form.cleaned_data['dep_name']
            dep_email = form.cleaned_data['dep_email']
            dep_phone =  form.cleaned_data['dep_phone']
            reasons = form.cleaned_data['reasons']

            print(form.data)   
            print(form.cleaned_data)
            # Save entry to database
            absence, created = Absence.objects.get_or_create(
                rehearsal=rehearsal,
                first_name=first_name,
                last_name=last_name,
                email=email,
                instrument=instrument,
                dep_name=dep_name,
                dep_email=dep_email,
                dep_phone=dep_phone,
                reasons=reasons
            )
            absence.save()
            
            # TODO send dep an email
            # if created = True:
                # send email dep

            return redirect_success(request, responses.ABSENCE_SUCCESS)

        else:
            return redirect_error(request, responses.ABSENCE_ERROR)
