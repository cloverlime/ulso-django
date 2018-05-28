from django.db import models
from django.utils import timezone

from .model_managers import *

from ulsosite.info.info import (
                   INSTRUMENT_LIST,
                   YEAR_LIST,
                   UNI_LIST,
                   DEFAULT_VENUE,
                   MEMBERSHIP_STATUS,
                   )
from ulsosite.info.dates import AUDITION_DATES_2017, CONCERTO_DATES_2017
# from ulsosite.models import Concert

class Person(models.Model):
    created = models.DateTimeField(editable=False, blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50, blank=True, null=True) # optional
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=30) # change this

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id or not self.created:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Person, self).save(*args, **kwargs)

    class Meta:
        abstract = True

class Musician(Person):
    instrument = models.CharField(max_length=20, choices=INSTRUMENT_LIST)
    doubling = models.CharField(max_length=50, default=None, blank=True) # optional
    uni = models.CharField(max_length=50, choices=UNI_LIST)
    other_uni = models.CharField(max_length=50, default=None, blank=True)
    status = models.CharField(max_length=30, choices=MEMBERSHIP_STATUS, default="Candidate")
    year = models.CharField(max_length=5, choices=YEAR_LIST)
    experience = models.TextField(default='Briefly summarise your recent orchestral experience')
    returning_member = models.BooleanField(default=False)
    subs_paid = models.BooleanField(default=False)

    def __repr__(self):
        return '{} {} ({})'.format(self.first_name, self.last_name, self.instrument)

    # Managers -------
    members = MemberManager()
    reserves = ReserveManager()
    candidate = CandidateManager()
    rejected = RejectedManager()
    # For individual instruments not listed here, use regular filters.
    wind = WindManager()
    brass = BrassManager()
    strings = StringsManager()
    percussion = PercussionManager()
    harps = HarpsManager()

    class Meta:
        ordering = ['instrument']


class AuditionSlot(models.Model):
    musician = models.OneToOneField('Musician', null=True, on_delete=models.SET_NULL)
    audition_date = models.CharField(max_length=30, choices=AUDITION_DATES_2017, blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

class ConcertoApplicant(Person):
    instrument = models.CharField(max_length=20, choices=INSTRUMENT_LIST)
    pieces = models.TextField()
    years_ulso_member = models.CharField(max_length=50, help_text="e.g. 2015-2017")
    notes = models.TextField(blank=True)
    second_round = models.BooleanField(default=False, help_text='Admitted to 2nd round')

    # Managers
    no_shortlist = NoSecondRoundManager()
    shortlisted = SecondRoundManager()

class ConcertoAuditionRound(models.Model):
    musician = models.ForeignKey('ConcertoApplicant', null=True, on_delete=models.SET_NULL)
    audition_date = models.CharField(max_length=30, choices=CONCERTO_DATES_2017, blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    # success = models.BooleanField(default=False)

class ConcertoWinner(Person):
    website = models.URLField()
    biography = models.TextField()

class CommitteeMember(Person):
    def __repr__(self):
        return '{} ({} {}) - {}'.format(self.role,
                                       self.first_name,
                                       self.last_name,
                                       self.season)
    instrument = models.CharField(max_length=20, choices=INSTRUMENT_LIST)
    uni = models.CharField(max_length=50, choices=UNI_LIST)
    role = models.CharField(max_length=100)
    season = models.CharField(max_length=10, default='2017/18', help_text='Format yyyy/yy')
    role_description = models.TextField(max_length=1000, help_text="Introduce yourself and tell people a bit about your role in ULSO.")

    class Meta(Person.Meta):
        ordering = []


class Conductor(Person):
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    phone = models.CharField(max_length=30, blank=True, help_text="Although this field is not marked as required, it is strongly recommended that you have a record of this.")
    website = models.URLField(blank=True)
    rate_per_rehearsal = models.IntegerField(default=125, help_text="Fee charged per 3 hour rehearsal.")
    rate_concert_day = models.IntegerField(default=500, help_text="If only the price of the entire project was agreed, put zero per rehearsal and enter the entire fee here")
    notes = models.TextField(blank=True)
