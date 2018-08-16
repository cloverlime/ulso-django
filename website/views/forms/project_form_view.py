import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

from ulsosite.models.concerts import Concert
from website.forms.project_signup import ProjectSignUp

class ProjectFormView(View):
    form_template = 'website/pages/project-signup-page.html'
    concert = Concert.objects.get(current=True)
    title = f"Project Sign-Up"

    def post(self, request):
        # form = ProjectSignUp(data=request.POST)
        pass

    def get(self, request):
        form = ProjectSignUp()
        context = {
            'form': form,
            'title': self.title,
            'concert': self.concert,
        }
        return render(request, self.form_template, context)