from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

def clear_messages(request):
    storage = messages.get_messages(request)
    storage.used = True
    return

def redirect_success(request, response):
    clear_messages(request)
    messages.add_message(request, messages.SUCCESS, response)
    return redirect(reverse('form_success'))

def redirect_error(request, response):
    clear_messages(request)
    messages.add_message(request, messages.ERROR, response)
    return redirect(reverse('form_error'))