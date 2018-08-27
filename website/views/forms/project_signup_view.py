import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

from ulsosite.models.concerts import Concert, Absence, Rehearsal
from ulsosite.models.people import Musician

from website.forms.project_signup_form import ProjectSignUp
from website import responses
from website.utils import redirect_success, redirect_success


class ProjectFormView(View):
    form_template = 'website/pages/project-signup-page.html'
    success_template = 'website/forms/form-success.html'
    fail_template = 'website/forms/form-fail.html'

    def get_current_concert():
        return Concert.objects.filter(current=True)

    def get_current_rehearsal_set():
        return Rehearsal.objects.filter(concert=Concert.objects.filter(current=True))

    concert = get_current_concert()
    rehearsals = get_current_rehearsal_set()

    title = f"Project Sign-Up"

    def post(self, request):
        form = ProjectSignUp(data=request.POST)
        
        if form.is_valid():
            data = form.cleaned_data

            # Identify the musician
            try:
                musician = Musician.objects.get(
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    email=data['email']
                )
            except:
                return redirect_error(request, responses.CANNOT_MATCH_MUSICIAN)

            # If can't make the project, continue.
            if data['can_make_concert'] == 'Yes':
                # Add player to concert
                self.concert.players.add(musician)

                # For any absences, add to absence list
                for rehearsal in self.rehearsals:
                    if rehearsal not in data['attendance']:
                        # create absence
                        absence = Absence.objects.create(
                            rehearsal=rehearsal,
                            first_name=data['first_name'],
                            last_name=data['last_name'],
                            email=data['email'],
                            instrument=data['instrument'],
                            reasons="Submitted in project form",
                        )

                        if absence == None:
                            return redirect_error(request, responses.DATABASE_ERROR)

                        absence.save()

                return redirect_success(request, responses.PROJECT_SIGNUP_SUCCESS)

            else: # can't make concert
                return redirect_success(request, responses.PROJECT_NO_SIGNUP_SUCCESS) 

        else: # Invalid  or didn't choose any rehearsals
                return redirect_error(request, responses.PROJECT_SIGNUP_ERROR)
    
    def get(self, request):
        form = ProjectSignUp()
        context = {
            'form': form,
            'title': self.title,
            'concert': self.concert,
        }
        return render(request, self.form_template, context)
