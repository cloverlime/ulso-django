# WIP, DO NOT COMMIT

from datetime import datetime, timedelta, time
from django.core.management.base import BaseCommand, CommandError
from ulsosite.models.auditions import AuditionDate, AuditionSlot
from ulsosite.utils import academic_year_calc

class Command(BaseCommand):
    """Creates a timetable of audition empty slots for one particular day.
    Usage:

    python manage.py create_audition_timetable [start_time] [end_time] [slot_length]

    Format:

        date - dd/mm/yy e.g. 08/10/18
        [start_time] - 24h HH:MM, defaults to 10:00
        [end_time] - 24h HH:MM . defaults to 17:00
        [slot_length] - in minutes, defaults to 15

    Use defaults:
        python manage.py create_audition_slots 06/10/18

    Set custom parameters:
        python manage.py create_audition_slots 06/10/18 9:30 17:00 30

    """
    help = "HELP: Creates a timetable of audition empty slots for one particular day."

    def add_arguments(self, parser):
        parser.add_argument(
            'date',
            help="dd/mm/yy (required)"
        )
        parser.add_argument(
            'start_time',
            nargs='?',
            default="10:00",
            help="HH:MM, default 10:00"
        )
        parser.add_argument(
            'end_time',
            nargs='?',
            default="18:00",
            help="HH:MM, default 18:00"
        )
        parser.add_argument(
            'slot_length',
            nargs='?',
            default=15,
            type=int,
            help="minutes, below 60 and to nearest 5 min"
        )

    def handle(self, *args, **options):
        # Ensure date is in correct format
        try:
            date = datetime.strptime(options['date'], "%d/%m/%y") # convert to date_time
        except ValueError:
            print("Invalid date format, should be dd/mm/yy e.g. 25/03/18")
            return

        # Ensure start and end times are in correct format
        try:
            start_time = datetime.strptime(
                f"{options['date']} {options['start_time']}",
                "%d/%m/%y %H:%M"
            )
            end_time = datetime.strptime(
                f"{options['date']} {options['end_time']}",
                "%d/%m/%y %H:%M"
            )
        except ValueError:
            print("Invalid start or end time, should be HH:MM e.g. 15:30")
            return

        # Ensure slot lengths are a divisible by 5
        slot_length = options['slot_length']
        if slot_length % 5 != 0:
            print(f"Slots of {slot_length} minutes require some maths to keep track of. Perhaps do yourself a favour and choose a number that's divisible by 5. You might just thank me for it.")
            return
        elif slot_length > 60:
            print("Do you really want an audition that's more than an hour? This likely not suitable for ULSO. Contact webmaster@ulso.co.uk if you wish to discuss.")
            return

        # Calculate season from date
        season = academic_year_calc(date)

        # Calculate number of slots
        total_minutes = (end_time - start_time).seconds // 60
        slots = total_minutes // slot_length
        slot_time = timedelta(minutes=slot_length)

        # Create AuditionDate in database
        try:
            audition_date, created = AuditionDate.objects.get_or_create(date=date, season=season)
            if created == False:
                confirm = input("Audition date already exists. Do you wish to overwrite? (Y/n)")
                if confirm == 'Y':
                    print("Continuing to make slots.")
                else:
                    print("Aborted.")
                    return
        except:
            print("Could not create audition date.")

        # Create slots for the day
        for n in range(slots):
            new_slot, created = AuditionSlot.objects.get_or_create(
                date=audition_date,
                time=(start_time + (n * slot_time))
            )

        print(f"Success! Created {slots} slots starting on {start_time}!")
