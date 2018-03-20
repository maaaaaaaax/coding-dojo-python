# Create your views here.

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from django.contrib import messages

from models import *

# Create your views here.
def index(request):
    return render(request, 'survey_form/index.html')

def submit(request):
    print "Got POST info"

    if len(request.POST['name']) < 1:
        messages.warning(request, 'Name cannot be blank.')
        print "Name cannot be blank!"
    elif len(request.POST['comment']) < 1:
        messages.warning(request, 'Comment cannot be blank!')
        print "Comment cannot be blank!"
    elif len(request.POST['comment']) > 120:
        messages.warning(request, 'Comment cannot be more than 120 characters.')
        print "Comment cannot be more than 120 characters."
    else:
        messages.success(request, 'Your information was submitted successfully!')
        print "Success!"

    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']

    return redirect('/result')

def result(request):
    return render(request, 'survey_form/result.html')

def reset(request):
    print "You have logged out and cleared the session."
    session.clear()
    return redirect('/')
