import datetime
# from django.db import models

# from .models import Musician

# class AuditionSlot(models.Model):
#     date = models.DateField()
#     time = models.TimeField()
#     musician = models.OnetoOneField(Musician, on_delete=SET_NULL, null=True, blank=True)


class Timetable:
    """
    Creates a timetable in the form of a (nested) dictionary.
    """
    def __init__(self, slot_length, start_time, end_time, dates_list):
        self.slot_length: slot_length #in minutes
        self.start_time: start_time
        self.end_time: end_time
        self.dates_list: dates_list # a list of datetime dates

    def create_slots_per_day(self):
        list_of_slots = []
        total_minutes = (self.start_time - self.end_time).minutes # a timedelta, an integer
        number_of_slots = int(total_minutes / self.slot_length) # always rounds down
        for i in range(0, number_of_slots):
            list_of_slots.append(self.start_time + datetime.timedelta(minutes=self.slot_length))
        return list_of_slots

    def none_to_slots(self):
        """
        Assigns None to every slot, which will later be filled by a Musician objectself.
         Returns a dictionary along the lines of:
                        { '9:00': None,
                          '9:30: None',
                          '10:30: None,}
        """
        slots = create_slots_per_day(self)
        return { slot: None for slot in slots }

    # assuming slots are the same for each day...
    def create_timetable(self):
        none_assigned_slots = none_to_slots(self)
        timetable = {}
        return { date: slots for date in self.dates_list for for slots in none_assigned_slots}
