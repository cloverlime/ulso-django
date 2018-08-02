"""Populates tables with a small amount of fake data for development purposes.
Obviously, if the schema changes significantly then this won't work....
"""
from django.core.management.base import BaseCommand, CommandError
from ulsosite.models.people import Musician, CommitteeMember, Conductor
from ulsosite.models.concerts import Concert, Piece, Rehearsal

class Command(BaseCommand):

    def create_musicians():
        pass

    def create_committemembers():
        pass

    def create_conductors():
        pass

    def create_concerts():
        # include pieces and rehearsals
        pass


    def handle(self, *args, **options):
        confirm = input("Are you sure you want to add a bunch of fake data? Do NOT use this command in production. (Y/n) ")
        if confirm == 'Y':
            create_musicians()
            create_conductors()
            create_committemembers()
            create_concerts()
            print("Successfully created test entries for 10 musicians, 3 conductors, 5 committee members and 2 concerts.")

        else:
            print("Aborted")
            return
