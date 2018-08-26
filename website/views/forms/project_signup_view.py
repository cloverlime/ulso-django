import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

from ulsosite.models.concerts import Concert, Absence, Rehearsal
from ulsosite.models.people import Musician

from website.forms.project_signup_form import ProjectSignUp

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
            # Get cleaned data...
            data = form.cleaned_data

            # Identify the musician
            try:
                musician = Musician.objects.get(
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    email=data['email']
                )
            except:
                FAIL_MESSAGE = 'We don\t recognise you. Are you sure you entered your details as registered?'
                messages.add_message(request, messages.ERROR, FAIL_MESSAGE)
                return redirect(reverse('form_error'))

            # If can't make the project, continue.
            if data['can_make_concert'] == 'Yes':
                # Add player to concert
                self.concert.players.add(musician)

                # For any absences, add to absence list
                for rehearsal in self.rehearsals:
                    print(rehearsal)
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
                            messages.add_message(request, messages.ERROR, 'There was a internal error. Please report this to webmaster@ulso.co.uk!' )
                            return redirect(reverse('form_success'))

                        absence.save()

            else: # Can't make concert
                PROJECT_SIGNUP_SUCCESS = 'Thank you for signing up for our next project. We will contact you by email with further information.'
                messages.add_message(request, messages.SUCCESS, PROJECT_SIGNUP_SUCCESS)
                return redirect(reverse('form_success'))
                
            PROJECT_NO_SIGNUP_SUCCESS = 'Thank you for filling in our form. We\'re sorry to hear that you can\'t make it this time, but we hope to see you again soon.'
            messages.add_message(request, messages.SUCCESS, PROJECT_NO_SIGNUP_SUCCESS)
            return redirect(reverse('form_success'))

        else: # Invalid  or didn't choose any rehearsals
            messages.add_message(request, messages.ERROR, 'Your form could not be processed. Did you forget to select any rehearsals?' )
            return redirect(reverse('form_error'))
    
    def get(self, request):
        form = ProjectSignUp()
        context = {
            'form': form,
            'title': self.title,
            'concert': self.concert,
        }
        return render(request, self.form_template, context)
