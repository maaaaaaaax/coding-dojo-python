# Create your views here.

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

from models import *

# Create your views here.
def index(request):
    if 'counter' not in request.session:
        request.session['counter']=0
    # request.session['counter']+=1
    print "request.session['counter'] is {}".format(request.session['counter'])
    request.session['random_word'] = get_random_string(length=14)
    print request.session['random_word']
    return render(request, 'random_word/index.html')

def randomize(request):
    if 'counter' not in request.session:
        request.session['counter']=0
    request.session['counter']+=1
    print "request.session['counter'] is {}".format(request.session['counter'])
    return redirect('/')

def reset(request):
    request.session['counter']=0
    print "request.session['counter'] is {}".format(request.session['counter'])
    return redirect('/')
