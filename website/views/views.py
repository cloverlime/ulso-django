import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.contrib.messages import get_messages


from status.models import Status
from ulsosite.utils import academic_year_calc
from ulsosite.info.dates import CURRENT_SEASON

from ulsosite.models.concerts import (
    Concert,
    Piece,
    Rehearsal,
)
from ulsosite.models.auditions import AuditionDate

from ulsosite.models.people import (
    CommitteeMember,
    ConcertoWinner,
)

from website.models import (
    Page,
    Section,
    AccordionCard,
)

from ulsosite.info.dates import CURRENT_SEASON

def rehearsals(request):
    page = Page.objects.get(title="Rehearsals")
    current_concert = Concert.objects.get(current=True)
    pieces = current_concert.piece_set.all()
    rehearsals = current_concert.rehearsal_set.all()
    venue = current_concert.venue_set.first()
    # upcoming_concerts = Concert.objects.filter(current=False).order_by('date')
    context = {
        'concert': current_concert,
        'page': page,
        'pieces': pieces,
        'rehearsals': rehearsals,
        'venue': venue
    }
    return render(request, 'website/pages/rehearsals.html', context)

def about(request):
    page = Page.objects.get(title="About")
    accordion = page.accordioncard_set.all().order_by("order")
    season = CURRENT_SEASON
    committee = CommitteeMember.objects.all().filter(season=season).exclude(role="Chair")
    chair = CommitteeMember.objects.all().filter(season=season).filter(role="Chair")
    context = {
        'accordion': accordion,
        'page': page,
        'chair': chair,
        'committee': committee,
        'page': page,
        'season': season
    }
    return render(request, 'website/pages/about.html', context)

def join(request):
    applications_open = Status.objects.get(season=CURRENT_SEASON).auditions_open
    page = Page.objects.get(title="How to Join")
    accordion = page.accordioncard_set.all().order_by('order')
    season = CURRENT_SEASON
    audition_dates = AuditionDate.objects.filter(season=season)

    context = {
        'accordion': accordion,
        'page': page,
        'applications_open': applications_open,
        'audition_dates': audition_dates,
        'season': season,
    }
    return render(request, 'website/pages/join.html', context)

def media(request):
    return HttpResponse("ULSO's media page")

def concerto(request):
    season = CURRENT_SEASON
    last_season = academic_year_calc(
        datetime.datetime.now() - datetime.timedelta(days=365)
    )
    applications_open = Status.objects.get(season=season).concerto_open
    page = Page.objects.get(title="Concerto Competition")
    accordion = page.accordioncard_set.all().order_by("order")
    winners = ConcertoWinner.objects.filter(season=last_season)
    past_winners = ConcertoWinner.objects.exclude(season=last_season)
    context = {
        'page': page,
        'season': season,
        'last_season': last_season,
        'applications_open': applications_open,
        'accordion': accordion,
        'winners': winners,
        'past_winners': past_winners
    }
    return render(request, 'website/pages/concerto.html', context)

def whatson(request):
    page = Page.objects.get(title="What's On")
    current_concert = Concert.objects.get(current=True)
    current_pieces = current_concert.piece_set.all().order_by('order')
    concerts = Concert.objects.all().exclude(current=True).order_by('date')
    context = {
        'current_concert': current_concert,
        'page': page,
        'current_pieces': current_pieces,
        'concerts': concerts,
    }
    return render(request, 'website/pages/whatson.html', context)

def depping_policy(request):
    page = Page.objects.get(title="Depping Policy")
    return render(request, 'website/pages/page-simple.html', { 'page': page })

def privacy_policy(request):
    page = Page.objects.get(title="Privacy Policy")
    return render(request, 'website/pages/page-simple.html', { 'page': page })

def form_success(request):
    messages = get_messages(request)
    return render(request, 'website/forms/form-success.html', {'messages': messages})

def form_error(request):
    messages = get_messages(request)
    return render(request, 'website/forms/form-error.html', {'messages': messages})