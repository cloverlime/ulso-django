from django.db import models
from django.utils import timezone

from ulsosite.info.info import DEFAULT_VENUE

from .people import Conductor, Musician

from ulsosite.utils import format_time, format_date

class Concert(models.Model):
    def __str__(self):
        return '{} - {} - {}'.format(self.project_term, self.date, self.conductor)
    current = models.BooleanField(default=False)
    project_term = models.CharField(max_length=30, help_text="e.g. Autumn, Winter, Spring, Summer 1, Summer 2")
    start_time = models.TimeField(help_text="Start time of concert", default='19:00:00')
    date = models.DateField('concert date')
    conductor = models.ForeignKey(Conductor, on_delete=models.SET_NULL, blank=True, null=True)
    soloist = models.CharField(max_length=100, blank=True)
    soloist_website = models.CharField(max_length=200, blank=True)
    concert_venue = models.CharField(max_length=300, default=DEFAULT_VENUE)
    # player list
    player = models.ManyToManyField(Musician)

class Poster(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    poster = models.ImageField(null=True, blank=True, upload_to='posters')
    artist = models.CharField(max_length=30, help_text='name of the artist')
    website = models.CharField(max_length=200, blank=True, help_text="Artist's website, if exists")

# TODO Sort this out or put into a different app
class Piece(models.Model):
    def __str__(self):
        return '{} - {}'.format(self.composer, self.piece)

    def __repr__(self):
        return """{} - {}, {} mins,
            Wind: {}.{}.{}.{}
            Brass: {}.{}.{}.{}
            Strings: {}.{}.{}.{}
            Timps: {}
            Perc: {}
            Harps: {}
            Notes: {}
                   {}
                   {}
                   {}
        """.format(self.composer,
                    self.piece,
                    self.flutes,
                    self.clarinets,
                    self.oboes,
                    self.bassoons,
                    self.horns,
                    self.trumpets,
                    self.trombones,
                    self.tubas,
                    self.violin_1,
                    self.violin_2,
                    self.violas,
                    self.cellos,
                    self.basses,
                    self.timps,
                    self.percussionists,
                    self.harps,
                    self.wind_notes,
                    self.brass_notes,
                    self.strings_notes,
                    self.other,
                    )

    def return_orchestration(self):
        return self.__repr__

    concert = models.ManyToManyField(Concert, blank=True)
    composer = models.CharField(max_length=20, help_text='Surname only')
    piece = models.CharField(max_length=200, help_text='Name of piece')
    order = models.IntegerField(blank=True, help_text='The order of the piece in the concert e.g. 1')
    duration = models.IntegerField(default=0, help_text="Length in minutes",blank=True, null=True)

    # Orchestration
    flutes = models.IntegerField(blank=True, null=True)
    clarinets = models.IntegerField(blank=True, null=True)
    oboes = models.IntegerField(blank=True, null=True)
    bassoons = models.IntegerField(blank=True, null=True)
    wind_notes = models.CharField(blank=True, max_length=200, help_text='e.g. alto, picc, contra requirements')
    horns = models.IntegerField(blank=True, null=True)
    trumpets = models.IntegerField(blank=True, null=True)
    trombones = models.IntegerField(blank=True, null=True)
    tubas = models.IntegerField(blank=True, null=True)
    brass_notes = models.CharField(blank=True, max_length=200)
    violin_1 = models.IntegerField('First violins', blank=True, null=True)
    violin_2 = models.IntegerField('Second violins', blank=True, null=True)
    violas = models.IntegerField(blank=True, null=True)
    cellos = models.IntegerField(blank=True, null=True)
    basses = models.IntegerField('Double basses', blank=True, null=True)
    strings_notes = models.CharField(blank=True, max_length=200)

    harps = models.IntegerField(blank=True, help_text="Number of harps", null=True)
    timps = models.BooleanField(blank=True, default=True)
    percussionists = models.IntegerField(blank=True, default=3, help_text="Number of percussionists requried", null=True)
    other = models.TextField(blank=True, help_text="Equipment notes")


class Rehearsal(models.Model):
    """
    Each project has many rehearsals.
    Each rehearsal has one venue.
    Each rehearsal has an absence list, preferable pre-populated by forms filled
    in by players, but entries can be added manually too.

    """
    def __str__(self):
        return '{} {}-{}'.format(
            format_date(self.date),
            format_time(self.start_time),
            format_time(self.end_time)
        )
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    date = models.DateField('rehearsal date')
    start_time = models.TimeField(default='19:00:00')
    end_time = models.TimeField(default='22:00:00')
    rehearsal_venue = models.CharField(max_length=300, default=DEFAULT_VENUE)
    # venue = models.ManyToManyField(Venue)
    notes = models.CharField(max_length=400, blank=True)


class Absence(models.Model):
    """
    In each rehearsal, there will inevitably be some players who have to miss it.
    The orchestral manager needs to keep track of these.
    Ideally, the players would report these in advance.
    The players must already be in the list of players assigned to the concert.
    """
    def __str__(self):
        return self.full_name
    rehearsal = models.ForeignKey(Rehearsal, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=20, help_text="As registered")
    email = models.EmailField("Your email address", max_length=100, help_text="As registered")
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, blank=True, null=True)
    instrument = models.CharField(max_length=20)
    dep_name = models.CharField('Full name of dep', max_length=20, blank=True, null=True)
    dep_email = models.EmailField("Dep's email address", max_length=100, help_text="This is for us to notify your dep about our privacy policy, and gives them information on how to contact us if need be.", blank=True, null=True)
    dep_phone = models.CharField(max_length=20, blank=True, null=True, help_text="Please give us your dep's phone number if at all possible. We will only contact them in the case of unexpected events to do with the rehearsal.")
    reasons = models.TextField(max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField(editable=False, blank=True, null=True)

    def save(self, *args, **kwargs):
        ''' On receipt, create timestamps and assign to an existing Musician '''
        if not self.id or not self.timestamp:
            self.timestamp = timezone.now()
        # Try to reference musician from Musician database
        # TODO decide if this part goes in the form or not....
        if not self.musician:
            try:
                split = (self.full_name).split(' ')
                first_name = split[0]
                last_name = split[1]
                self.musician = Musician.candidates.get(
                    first_name=first_name,
                    last_name=last_name,
                    email=self.email
                )
            except:
                return super(Absence, self).save(*args, **kwargs)
        return super(Absence, self).save(*args, **kwargs)


# TODO - Currently not linked to anything - sort this out
class Venue(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=40, help_text="Official name e.g. 'St Stephen\'s Church'")
    address_1 =  models.CharField(max_length=200, help_text="First line of address")
    address_2 =  models.CharField(max_length=200, help_text="Second line of address", blank=True, null=True)
    email = models.EmailField(max_length=200)
    contact_number = models.CharField(max_length=10, blank=True, null=True)
    rate_per_rehearsal = models.IntegerField(default=90, help_text="Fee charged per 3 hour rehearsal.", blank=True, null=True)
    rate_concert_day = models.IntegerField(default=140, help_text="If only the price of the entire project was agreed, put zero per rehearsal and enter the entire fee here.", blank=True, null=True)
    rate_per_hour = models.IntegerField(default=90, help_text="Alternative to the above fee structures", blank=True, null=True)
