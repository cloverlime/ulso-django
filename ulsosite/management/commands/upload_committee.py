""" Result of an evening at codebar, do not commit"""

import argparse
import csv

from django.core.management.base import BaseCommand, CommandError
from ulsosite.models.people import CommitteeMember

class Command(BaseCommand):
    """Uploads one or more CSV files and creates new database entries. Assumes headers are on first line and match the model fields."""

    help = "Upload data from a CSV file into the database"

    def add_arguments(self, parser):
        parser.add_argument('filenames', nargs='+', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        for file in options['filenames']:
            # do it the manually if no header on first line
            # rows = csv.reader(file, delimiter='|')
            # for row in rows:
            #     self.stdout.write(row[0])
            #     { 'first_name' = row[0] }

            # If first row has headers:
            reader = csv.DictReader(file, delimiter='|')
            for row in reader: # row is an OrderedDict
                # print(row)
                # print(type(row))
                try:
                    entry, created = CommitteeMember.objects.get_or_create(
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
                    if created == True:
                        print(f"Added {row['first_name']} {row['last_name']} as {row['role']}")
                    else:
                        print(f"Updated {row['first_name']} {row['last_name']} as {row['role']}")
                except:
                    print(f"ERROR at {row['first_name']} {row['last_name']} as {row['role']}. This entry was not saved or updated. Contact webmaster@ulso.co.uk for help.")
                    continue
            #
            # text = file.readline()
            # self.stdout.write(text)
