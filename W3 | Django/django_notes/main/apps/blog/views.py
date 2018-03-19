from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "Thank you for visiting localhost:8000/blog/! This is placeholder text that will later display a list of blogs."
    return HttpResponse(response)

def new(request):
    response = "Placeholder to display a new form to create a new blog."
    return HttpResponse(response)

def create(request):
    return redirect('/')

def show(request, number):
    response = "Placeholder to display blog #{}".format(number)
    return HttpResponse(response)

def edit(request, number):
    response = "Placeholder to edit blog #{}".format(number)
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/blog')
