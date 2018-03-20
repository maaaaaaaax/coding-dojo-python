from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, localtime, strftime

from models import *

# Create your views here.
def index(request):
    print strftime("%A, %B-%d-%Y",localtime())
    clock_date = strftime("%A, %B %d, %Y",localtime())
    print strftime("%H:%M %p",localtime())
    clock_hour_minute = strftime("%H:%M %p %Z",localtime())

    context = {
        # "SOME_KEY_NAME" : some_value
        "clock_date":clock_date,
        "clock_hour_minute":clock_hour_minute
    }
    return render(request, 'time_display/index.html', context)
