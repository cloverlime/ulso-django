import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

from ulsosite.models.concerts import Concert, Absence
from ulsosite.models.people import Musician

from website.forms.project_signup import ProjectSignUp

class ProjectFormView(View):
    form_template = 'website/pages/project-signup-page.html'
    success_template = 'websites/forms/form-success.html'
    concert = Concert.objects.get(current=True)
    title = f"Project Sign-Up"

    def post(self, request):
        form = ProjectSignUp(data=request.POST)
        
        if form.is_valid():
            # Get cleaned data...
            data = form.cleaned_data

            # Identify the musician
            musician = Musician.objects.get(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email']
            )

            # If can't make the project, continue. 
            if data['can_make_concert'] == 'Yes:
                # Add player to concert

                # For any absences, add to absence list

            context = {
                'message': 'Thank you for signing up for our next project. We will contact you by email with further information.'
            }
            return render(request, self.success_template, context)
        else:
            return HttpResponse("There was an error. Please report it to webmaster@ulso.co.uk")
    
    
    def get(self, request):
        form = ProjectSignUp()
        context = {
            'form': form,
            'title': self.title,
            'concert': self.concert,
        }
        return render(request, self.form_template, context)