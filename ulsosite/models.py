from django.db import models


class Concert(models.Model):
    season = models.CharField(max_length=100)
    concert_date = models.DateTimeField('concert date')
    conductor = models.CharField(max_length=100)
    conductor_website = models.CharField(max_length=300)
    soloist = models.CharField(max_length=100, default=None)
    soloist_website = models.CharField(max_length=300, default=None)
    concert_venue = models.CharField(max_length=300)


class Piece(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    composer = models.CharField(max_length=30)
    piece = models.CharField(max_length=200)
    order = models.IntegerField()


class Rehearsals(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    rehearsal_date = models.DateTimeField('rehearsal date')
    rehearsal_venue = models.CharField(max_length=300)
    notes = models.CharField(max_length=400)


class Committee(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    instrument = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    role_description = models.CharField(max_length=500)


class ConcertoWinner(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=300)
    instrument = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    biography = models.CharField(max_length=1000)
