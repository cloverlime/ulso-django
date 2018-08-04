import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage, BadHeaderError
from django.urls import reverse
from django.views import View

from website.forms import AuditionSignUp

# from ulsosite.utils import academic_year_calc

# def signup(request):
#     form = SignUp()
#     context = {'form': form}
#     return render(request, 'ulsosite/signup.html', context)
#     # return HttpResponse("Here is the page for signing up for an audition")

class SignUpView(View):
    form_class = AuditionSignUp
    form_template = 'website/signup.html'
    success_template = 'website/signup-success.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        context = { 'form': form }
        return render(request, self.form_template , context)

    def post(self, request, *args, **kwargs):
        # Create a form instance and populate it with data from the request (binding):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return render(request, self.success_template)
        else:
            return HttpResponse("Form wasn't valid")
