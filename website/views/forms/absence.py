import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from website.forms import AbsenceForm

from .generic import GenericFormView

class AbsenceFormView(GenericFormView):
    form_title = 'Absence'
    form_class = AbsenceForm
