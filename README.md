# ULSO-Django

Student Orchestra Management Tool and Website

### Introduction

**ulso-django** is a Django app that is a management tool and public website rolled into one. It is designed to expedite the organisation of the University of London Symphony Orchestra (ULSO), a professionally-conducted multi-collegiate student orchestra in London, UK.

ulso-django is currently a work in progress. For more information about the orchestra, the current static site (HTML/CSS/Bootstrap) can be viewed at http://ulso.co.uk.

### Architecture and Design

ulso-django is built using Django only.

It exists for now in a single app, but conceptually deals with two separate concerns:

1. The public-facing website
2. A private management suite


###### Public Site

The public site is a small website containing information about the orchestra (and in the future, some more media). Its Django-powered form will have a simple content management system (CMS) for easy editing of content, and rehearsal and concert information will be automatically updated. This should result in giving more power to the committee to edit the website and make the system more robust as the HTML/template code will no longer need to be changed (and potentially broken).

###### Management Suite

The management suite is where the impact will be the greatest. Django's built-in administration tools will be a large part of this.

The orchestra's current tool is the Google Admin Suite, which has created problems and confusion when different files resided in different Drives and constantly required configuring sharing options.

ulso-django seeks to put all management-related information in one organised and easily-searchable place, and provide as many shortcuts as possible for common actions.

#### Model Structure

The following contains the models used in for the suite. but does not show detailed relations.

The hierarchical representation below aims to show how they are grouped conceptually. The names inside asterisks are conceptual groupings only; their children are models. Anything in square brackets means it is planned but not yet implemented.

```
[ulso-django]
|
|── *People*
|     |── Musician
|     |── Conductor
|     |── Committee Member
|     └── Useful Contacts
|
|── *Projects*
|     └── Concert
|            |── Rehearsal
|            |      └── Absence
|            |── Piece
|            └── Venue
|
|── *Auditions*
|     |── Audition Date
|     └── Audition Slot
|
|── *CMS*
|     └── Page
|            |── Section
|            └── [ImageSection]
|
└── *Budget*
      |── Accounts
      └── [BudgetPlan]
```

### Custom Management Commands

Create empty audition timetables:

    python manage.py create_audition_slots date [start_time] [end_time] [slot_length]

To see help text, type:

    python manage.py <command> --help

### Run tests

To run all tests (or in a specific app):

    python manage.py test [app_name]

Increase verbosity:

    python manage.py test -v 2


### Priorities

###### Usability

Usability is the number concern for both the website and the management tool.

For the website, the goal is to communicate information in a direct, succinct and transparent way so any potential players come away with a clear and accurate idea of the orchestra (and hopefully persuade them to join).

For the management tool, the goal is to let the orchestra's committee spend as little time as possible doing anything repetitive or menial, such as searching for player information, creating project lists, absence lists and making audition schedules.

It is vitally important for the system to be easy to learn and intuitive and robust as possible.

###### Scalability and Performance

Scalability and performance are not so much of an issue. The player list and committee line-up refresh every year, there is no user-generated content on the website, and the size and complexity of the system is expected to remain roughly constant. For this reason, Django's templating system was deemed more than sufficient for the purposes of the website.

###### Maintainability

Having said the above, it is still important for the codebase to be as clearly organised, modular and easy to tweak as possible to accommodate new features, different committee preferences and potential changes to the orchestra's financial model.

### Feedback and Improvements

If you have any feedback, suggestions or just want to get in touch, don't hesitate to drop me a line at wenye.zhao@gmail.com.
