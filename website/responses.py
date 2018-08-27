# Generic
INVALID_FORM = 'Sorry, your form was invalid. Please make sure you have entered all details correctly and try again.'
BAD_HEADER = 'Invalid header. Email was not sent.'
DATABASE_ERROR = 'There was a database error. Please report this to webmaster@ulso.co.uk.'

CONTACT_SUCCESS = """
    Thank you for your interest in ULSO.
    We have received your message and will endeavour
    to get back to you as soon as possible."""
CONTACT_ERROR = INVALID_FORM

AUDITION_SIGNUP_SUCCESS = 'Thank you for signing up to ULSO.'
AUDITION_SIGNUP_ERROR = ''

ABSENCE_SUCCESS = 'Thank you for letting us know. We\'re sorry to miss you this time. Please note that if you are a wind, brass or percussion player, or a string leader, you must provide a dep.'
ABSENCE_ERROR = INVALID_FORM

PROJECT_SIGNUP_SUCCESS = 'Thank you for signing up for our next project. We will contact you by email with further information.'
PROJECT_NO_SIGNUP_SUCCESS = 'Thank you for filling in our form. We\'re sorry to hear that you can\'t make it this time, but we hope to see you again soon.'
PROJECT_SIGNUP_ERROR = 'Your form could not be processed. Did you forget to select any rehearsals?'

CONCERTO_SIGNUP_SUCCESS = 'Thank you for your submission. We will get back to you soon.'
CONCERTO_SIGNUP_ERROR = INVALID_FORM

CANNOT_MATCH_MUSICIAN = 'We don\t recognise you. Are you sure you entered your details as registered?'


# EMAIL_TO_DEP = f"""
# Dear {dep_first_name},

# You have received this email because {first_name } {last_name} has nominated you 
# as dep on {instrument} for ULSO's rehearsal on {rehearsal.time} {rehearsal.date}.

# We will be rehearsing one or more of the following pieces:

# {piece1}
# {piece2}
# {piece3}

# Please ask {first_name} for specifics.

# On the day, please contact {orchestral_manager.first_name} at {orchestral_manager.email}
# or {orchestral_manager.phone} if you run into any trouble.

# Thank you very much for agreeing to dep with is. It helps us a lot and I hope you enjoy your time.
# If you have any other questions or feedback, please contact {orchestral_manager} with the details above.

# Best wishes,

# ULSO
# """
