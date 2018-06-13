***************
ULSO Spec
***************

Kind of like the user stories but more technical, and grouped by subject rather than committee role.


===========
Overview
===========

The **django-ulso** projects aims to provide an admin suite for the efficient management of a student symphony orchestra. Specifically, it is designed for an orchestra that holds auditions annually, and whose committee refreshes yearly.

Its main goal is to expedite repetitive tasks: essentially, to remove all sources of inefficiency that is not to do with waiting for people to respond.

As of version 1.0, django-ulso is meant to complement ULSO's Google Admin Suite, which handles @ulso.co.uk email addresses and their respective Google Drives.


===========
Auditions
===========

The main bulk of committee work is managing people. Before the start of the first project, players must first be auditioned before they can gain membership. Roughly 200 applicants are expected.

Players are to sign up for an audition by submitting a form on the website. As well as obvious things like name, instrument, email address, the form **must** include:

* Phone number (important for musicians as this means we can contact them if they don't show up)
* University
* Depping policy agreement
* Privacy policy agreement (GDPR-compliant)
* Audition availability

Scheduling auditions:

* View timetable by day, instrument
* Can bulk-mark people as member, rejected, reserve etc.


Be able to:

* Create entire SET of empty audition slots for a given dates.
   * arguments include: date, start time, end time, interval (length of an audition).


=======
People 
=======



===========
Concerts
===========




Repertoire
===========





=======
Budget
=======







