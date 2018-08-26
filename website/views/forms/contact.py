from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage, BadHeaderError
from django.urls import reverse
from django.views import View

from website.models import Page

from ulsosite.models.people import (
    CommitteeMember,
    ConcertoWinner,
)
from ulsosite.info.dates import CURRENT_SEASON

from website.templates.messages.messages import CONTACT_MESSAGE_SUCCESS
from website.forms.contact import ContactForm

def contact(request):
    """
    Logic for the website's contact form. Sends an email directly to committee members' role@ulso.co.uk email addresses depending on the topic chosen by the sender.
    """
    if request.method == 'GET':
        page = Page.objects.get(title="Contact Us")
        form = ContactForm()
        form_text = '<h2>Contact Form</h2>'
        committee_member = CommitteeMember.objects.all().filter(season=CURRENT_SEASON)
        context = {
            'committee_members': committee_member,
            'form': form,
            'form_text': form_text,
            'page': page
        }
        return render(request, 'website/pages/contact.html', context)

    else:
        form = ContactForm(request.POST)

        # Validate form data
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            topic = form.cleaned_data['topic']
            full_subject = topic.upper() + ': ' + form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_self = form.cleaned_data['send_self']
            recipients = ['chair@ulso.co.uk']
            contact_address_dict = {
                'Auditions':       ['orchestra.manager@ulso.co.uk'],
                'Late/Absent':     ['orchestra.manager@ulso.co.uk'],
                'Percussion hire': ['orchestra.manager@ulso.co.uk', 'treasurer@ulso.co.uk'],
                'Conducting':      [],
                'Concerto':        ['orchestra.manager@ulso.co.uk'],
                'Publicity':       ['publicity@ulso.co.uk'],
                'Sponsorship':     ['treasurer@ulso.co.uk', 'sponsorship@ulso.co.uk'],
                'Concert Queries': ['orchestra.manager@ulso.co.uk'],
                'Subs':            ['treasurer@ulso.co.uk'],
                'Website':         ['webmaster@ulso.co.uk'],
                'Other':           []
            }

            # Direct email to appropriate address depending on topic
            recipients += contact_address_dict[topic]

            if send_self:
                cc_self = [email]
            else:
                cc_self=None

            email_msg = EmailMessage(
                full_subject, message,
                from_email=email,
                to=recipients,
                cc=cc_self
            )

            try:
                email_msg.send()

            except BadHeaderError:
                return HttpResponse("Invalid header found. Email was not sent.")

            # Redirect back to contacts page with a success message
            # TODO change to proper redirect

            messages.add_message(request, messages.SUCCESS, CONTACT_MESSAGE_SUCCESS)
            return redirect(reverse('form_success'))

        # Form is not valid
        else:
            messages.add_message(
                request, messages.ERROR,
                'Sorry, something went wrong. Please try again. Did you fill in all the details correctly?'
                )
            return redirect(reverse('form_error'))
