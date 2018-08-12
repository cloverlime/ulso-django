import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View

from ulsosite.utils import academic_year_calc
from ulsosite.info.dates import CURRENT_SEASON

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

CURRENT_SEASON = "2018/19"

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
    page = Page.objects.get(title="Committee")
    committee = CommitteeMember.objects.all().filter(season=season).exclude(role="Chair")
    chair = CommitteeMember.objects.all().filter(season=season).get(role="Chair")
    context = {
        'accordion': accordion,
        'page': page,
        'chair': chair,
        'committee': committee,
        'page': page,
        'season': season
    }
    return render(request, 'website/pages/about.html', context)

# def committee(request):
#     season = CURRENT_SEASON
#     page = Page.objects.get(title="Committee")
#     # chair = CommitteeMember.objects.get(role="Chair", season=academic_year_calc(datetime.now()))
#     committee = CommitteeMember.objects.all().filter(season=season).exclude(role="Chair")
#     chair = CommitteeMember.objects.all().filter(season=season).get(role="Chair")
#     context = {
#         'chair': chair,
#         'committee': committee,
#         'page': page,
#         'season': season
#     }
#     return render(request, 'website/committee.html', context)


def join(request):
    page = Page.objects.get(title="How to Join")
    accordion = page.accordioncard_set.all().order_by('order')
    context = {
        'accordion': accordion,
        'page': page
    }
    return render(request, 'website/pages/join.html', context)

def media(request):
    return HttpResponse("ULSO's media page")

def concerto(request):
    page = Page.objects.get(title="Concerto Competition")
    accordion = page.accordioncard_set.all().order_by("order")
    winners = ConcertoWinner.objects.filter(season="2016/17")
    past_winners = ConcertoWinner.objects.exclude(season="2016/17")
    context = {
        'page': page,
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
