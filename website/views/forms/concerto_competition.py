import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage, BadHeaderError
from django.urls import reverse
from django.views import View

from ulsosite.utils import academic_year_calc

from website.forms import ConcertoForm

class ConcertoSignUp(SignUpView):
    form_class = ConcertoForm
