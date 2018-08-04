import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage, BadHeaderError
from django.urls import reverse
from django.views import View

from ulsosite.utils import academic_year_calc

from website.forms import (
                    AuditionSignUp,
                    ContactForm,
                    ConcertoForm,
                    )

from ulsosite.models.concerts import (
                        Concert,
                        Piece,
                        Rehearsal,
                        )

from ulsosite.models.people import (
                        CommitteeMember,
                        ConcertoWinner,
                        )

from website.models import (
                        Page,
                        Section,
                        AccordionCard,
                        )



def signup_success(request):
    return HttpResponse("Thank you for signing up. We will get back to you soon.")
