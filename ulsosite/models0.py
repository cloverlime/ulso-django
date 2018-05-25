from django.db import models

from ulsosite.info import (INSTRUMENT_LIST,
                   YEAR_LIST,
                   UNI_LIST,
                   DEFAULT_VENUE,
                   MEMBERSHIP_STATUS,
                   AUDITION_DATES,
                   )


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50, blank=True, null=True) # optional
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=30, default="0XXXX XXXXXX") # change this
    instrument = models.CharField(max_length=20, choices=INSTRUMENT_LIST)
    doubling = models.CharField(max_length=50, default=None, blank=True) # optional
    uni = models.CharField(max_length=50, choices=UNI_LIST)
    other_uni = models.CharField(max_length=50, default=None, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        abstract = True
        ordering = ['instrument']


class Musician(Person):
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=MEMBERSHIP_STATUS, default="Candidate")
    # season = models.CharField(max_length=10, blank=True, help_text="Academic year currently or last registered e.g. 2017/18")
    year = models.CharField(max_length=5, choices=YEAR_LIST)
    experience = models.TextField(default='Briefly summarise your recent orchestral experience')
    returning_member = models.BooleanField(default=False)
    subs_paid = models.BooleanField(default=False)
    share_details = models.BooleanField("Share contact details", default=False, help_text="Occasionally, other orchestras in London may ask us for contact details of players for recruitment. To give ULSO permission to share your contact details, tick this box. We may also openly share playing opportunities, in which case players may choose to contact the orchestras directly. ")

    def __repr__(self):
        return '{} {} ({})'.format(self.first_name, self.last_name, self.instrument)


class AuditionApplicant(Musician):
    audition_date = models.CharField(max_length=30, choices=AUDITION_DATES, blank=True)
    audition_time = models.CharField(max_length=30, choices=AUDITION_TIMES, blank=True)


class ConcertoApplicant(Person):
    # date = models.DateTimeField('date submitted')
    pieces = models.TextField()
    years_ulso_member = models.CharField(max_length=50, help_text="e.g. 2015-2017")
    notes = models.TextField(blank=True)
    second_round = models.BooleanField(default=False, help_text='Admitted to 2nd round')


class ConcertoWinner(Person):
    website = models.URLField()
    biography = models.TextField()


class CommitteeMember(Person):
    def __repr__(self):
        return '{} ({} {}) - {}'.format(self.role,
                                       self.first_name,
                                       self.last_name,
                                       self.season)
    role = models.CharField(max_length=100)
    season = models.CharField(max_length=10, default='2017/18', help_text='Format yyyy/yy')
    role_description = models.TextField(max_length=1000, help_text="Description provided by personally by the committee member")

    class Meta(Person.Meta):
        ordering = []


class Conductor(models.Model):
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    website = models.URLField(blank=True)
    email = models.EmailField(max_length=100, blank=True, help_text='This field is not required to facilitate quick fill-in. However, it is highly advised for you fill this in ASAP.')
    phone = models.CharField(max_length=30, blank=True) # change this
    rate_per_rehearsal = models.IntegerField(default=125, help_text="Fee charged per 3 hour rehearsal.")
    rate_concert_day = models.IntegerField(default=500, help_text="If only the price of the entire project was agreed, put zero per rehearsal and enter the entire fee here")
    notes = models.TextField(blank=True)
