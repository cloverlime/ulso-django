from django.db import models

DEFAULT_VENUE = "St. Stephen's Church, Gloucester Road, SW7 4RL"

class Concert(models.Model):
    season = models.CharField(max_length=100)
    concert_date = models.DateTimeField('concert date')
    conductor = models.CharField(max_length=100)
    conductor_website = models.CharField(max_length=300, blank=True)
    soloist = models.CharField(max_length=100, blank=True)
    soloist_website = models.CharField(max_length=300, blank=True)
    concert_venue = models.CharField(max_length=300, default=DEFAULT_VENUE)

class Piece(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    composer = models.CharField(max_length=30)
    piece = models.CharField(max_length=200)
    order = models.IntegerField()


class Rehearsals(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    rehearsal_date = models.DateTimeField('rehearsal date')
    rehearsal_venue = models.CharField(max_length=300)
    notes = models.CharField(max_length=400, blank=True)


class Committee(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    instrument = models.CharField(max_length=100)
    uni = models.CharField(max_length=100)
    role_description = models.CharField(max_length=500)


class ConcertoWinner(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=300)
    instrument = models.CharField(max_length=100)
    uni = models.CharField(max_length=100)
    biography = models.CharField(max_length=1000)
