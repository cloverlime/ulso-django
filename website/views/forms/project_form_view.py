import datetime
import pprint as pp
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

from ulsosite.models.concerts import Concert, Absence
from ulsosite.models.people import Musician

from website.forms.project_signup import ProjectSignUp

class ProjectFormView(View):
    form_template = 'website/pages/project-signup-page.html'
    success_template = 'website/forms/form-success.html'
    fail_template = 'website/forms/form-fail.html'

    # TODO may want to change the concert query!
    concert = Concert.objects.get(current=True)
    rehearsals = concert.rehearsal_set.all()

    title = f"Project Sign-Up"

    def post(self, request):
        form = ProjectSignUp(data=request.POST)
        
        if form.is_valid():
            # Get cleaned data...
            data = form.cleaned_data
            pp.pprint(data)

            # Identify the musician
            try:
                musician = Musician.objects.get(
                    first_name=data['first_name'],
                    last_name=data['last_name'],
                    email=data['email']
                )
            except:
                context = {
                    'message': 'We don\t recognise you. Are you sure you entered your details as registered?'
                        }
                return render(request, self.fail_template, context)

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
                            context = {
                                'message': 'There was a internal error. Please report this to webmaster@ulso.co.uk!'
                            }
                            return render(request, self.fail_template, context)
                        
                        absence.save()

                context = {
                    'message': 'Thank you for signing up for our next project. We will contact you by email with further information.'
                }
            else: # Can't make concert
                context ={
                    'message': 'Thank you for filling in our form. We\'re sorry to hear that you can\'t make it this time, but we hope to see you again soon.'
                }    
            return render(request, self.success_template, context)
        else: # Invalid  or didn't choose any rehearsals
            context ={
                'message': 'Your form could not be processed. Did you forget to select any rehearsals?'
            }    
            return render(request, self.fail_template, context)
    
    
    def get(self, request):
        form = ProjectSignUp()
        context = {
            'form': form,
            'title': self.title,
            'concert': self.concert,
        }
        return render(request, self.form_template, context)