import argparse
import csv

from django.core.management.base import BaseCommand, CommandError
from ulsosite.models.people import Musician

class Command(BaseCommand):
    help = "Upload data from a CSV file into the Musician database"

    def add_arguments(self, parser):
        parser.add_argument('filenames', nargs='+', type=argparse.FileType('r'))

    def handle(self, *args, **options):
        total = 0
        errors = 0
        for file in options['filenames']:
            try:
                data = csv.DictReader(file, delimiter='|')
            except:
                raise CommandError(f"ERROR: could not read {file}.")
                continue

            for row in data: # row is an OrderedDict
                try:
                    entry, created = Musician.objects.get_or_create(
                        first_name=row['first_name'],
                        last_name=row['last_name'],
                        alias=row['alias'],
                        email=row['email'],
                        phone=row['phone'],
                        instrument=row['instrument'],
                        uni=row['uni'],
                        role=row['role'],
                        season=row['season'],
                        instrument=row['instrument'],
                        doubling=row['doubling'],
                        uni=row['uni'],
                        other_uni=row['other_uni'],
                        status=row['status'],
                        year=row['year'],
                        experience=row['experience'],
                        returning_member=row['returning_member'],
                        subs_paid=row['subs_paid'],
                        depping_policy=row['depping_policy'],
                        privacy_policy=row['privacy_policy'],
                    )
                    entry.save()
                    total += 1
                except:
                    errors += 1
            print(f"Finished loading {file}")
        # Uploaded all files
        print(f"Upload finished with {total} entries and {errors} errors.")
