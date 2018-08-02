from django.core.management.base import BaseCommand, CommandError
from ulsosite.models.people import Musician, CommitteeMember

class Command(BaseCommand):
    help = 'Deletes old data as per pour privacy policy.'

    def handle:
        pass
