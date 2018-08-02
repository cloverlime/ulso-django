import argparse
import csv

from django.core.management.base import BaseCommand, CommandError
from ulsosite.models.people import Musician

class Command(BaseCommand):
    help = "Upload data from a CSV file into the Musician database"

    def add_arguments(self, parser):
        parser.add_argument('filenames', nargs='+', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        self.stdout.write("Upload works!")
        for file in options['filenames']:
            # do it the manually if no header on first line
            # rows = csv.reader(file, delimiter='|')
            # for row in rows:
            #     self.stdout.write(row[0])
            #     { 'first_name' = row[0] }


            reader = csv.DictReader(file, delimiter='|')
            for row in reader: # row is an OrderedDict
                print(row)
                print(type(row))

                entry = CommitteeMember.objects.create(
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    alias=row['alias'],
                    email=row['email'],
                    phone=row['phone'],
                    instrument=row['instrument'],
                    uni=row['uni'],
                    role=row['role'],
                    season=row['season'],
                    description=row['description']
                )
                entry.save()

            # text = file.readline()
            # self.stdout.write(text)
