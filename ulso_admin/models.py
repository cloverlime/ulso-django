from django.db import models

from ulsosite.info import (INSTRUMENT_LIST,
                   YEAR_LIST,
                   UNI_LIST,
                   DEFAULT_VENUE
                   )


class Person(models.Model):
    def __str__(self):
        return '{} {} ({})'.format(self.first_name, self.last_name, self.instrument)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50, default=None, blank=True) # optional
    email = models.EmailField(max_length=100)
    instrument = models.CharField(max_length=1, choices=INSTRUMENT_LIST)
    doubling = models.CharField(max_length=50, default=None, blank=True) # optional
    uni = models.CharField(max_length=1, choices=UNI_LIST)
    other_uni = models.CharField(max_length=50, default=None, blank=True)

    class Meta:
        abstract = True
        ordering = ['instrument']

class Musician(Person):
    # date = models.DateTimeField('date entered')
    member = models.BooleanField(default=False, help_text="Admitted to ULSO y/n")
    season = models.CharField(max_length=10, blank=True, help_text="Academic year currently or last registered e.g. 2017/18")
    year = models.CharField(max_length=1, choices=YEAR_LIST)
    experience = models.TextField(default='Briefly summarise your recent orchestral experience')
    returning_member = models.BooleanField(default=False)
    subs_paid = models.BooleanField(default=False)


class ConcertoApplicant(Person):
    # date = models.DateTimeField('date submitted')
    year = models.CharField(max_length=1, choices=YEAR_LIST)
    pieces = models.TextField()
    years_ulso_member = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    second_round = models.BooleanField(blank=True, default=False)


class ConcertoWinner(Person):
    website = models.CharField(max_length=300)
    biography = models.TextField()


class CommitteeMember(Person):
    def __str__(self):
        return '{}({} {}) - {}'.format(self.role,
                                       self.first_name,
                                       self.last_name,
                                       self.season)
    season = models.CharField(max_length=10, default='2017/18', help_text='Format yyyy/yy')
    role = models.CharField(max_length=100)
    role_description = models.CharField(max_length=1000, help_text="Description provided by personally by the committee member")

    class Meta(Person.Meta):
        ordering = []


class Conductor(models.Model):
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    website = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True, help_text='This field is not required to facilitate quick fill-in. However, it is highly advised for you fill this in ASAP.')
    phone = models.CharField(max_length=15, blank=True) # change this
    rate_per_rehearsal = models.IntegerField(default=125, help_text="Fee charged per 3 hour rehearsal.")
    rate_concert_day = models.IntegerField(default=500, help_text="If only the price of the entire project was agreed, put zero per rehearsal and enter the entire fee here")
    notes = models.TextField(blank=True)

# class Orchestration(models.Model):
#     duration = models.IntegerField(blank=True, help_text="Length in minutes")
#     wind = models.CharField(blank=True, max_length=10, help_text="e.g. 3.4.3.3 for flutes.clarinets.oboes.bassoons")
#     brass = models.CharField(blank=True, max_length=10, help_text="e.g. 4.2.2.0 for horns.trumpets.trombones.tubas")
#     strings = models.CharField(blank=True, max_length=10, help_text="e.g. 10.8.6.5.3 for vln1.vln2.vla.vc.bass")
#     harps = models.IntegerField(blank=True, default=0, help_text="Number of harps")
#     timps = models.BooleanField(blank=True, default=True)
#     percussionists = models.IntegerField(blank=True, default=3, help_text="Number of percussionists requried")
#     percussion_equipment = models.CharField(max_length=300, blank=True, help_text="Brief description of percussion equipment required")
#     other = models.TextField(blank=True)
