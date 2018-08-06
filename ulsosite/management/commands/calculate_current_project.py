from datetime import datetime, timedelta, time
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError

from ulsosite.models.concerts import Concert
from ulsosite.utils import academic_year_calc

class Command(BaseCommand):
    def handle(self, *args, **options):
        """A command to be run daily to check which project is the current one."""

        # Remove 'current' from all concerts
        current_projects = Concert.objects.filter(current=True)
        for project in current_projects:
            project.current = False
            project.save()

        today = timezone.now()
        current_season = academic_year_calc(today)
        # season_concerts = Concert.objects.filter(season=curent_season).order_by('date')

        if season_concerts = None:
            # If no concerts/projects exist, quit immediately
            print(f"Did not find any concerts in {current_season}")
            return

        for concert in season_concerts:
            # Is today's date before concert1?
            if today < concert.date:
                concert.current = True
                concert.save()
            else:
                continue

        # Is today's date before concert1?
            # No, move to next..
            # Is today before concert2?
            # Yes, so concert 2 is current.
