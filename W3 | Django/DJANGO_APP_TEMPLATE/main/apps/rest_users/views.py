# Create your views here.

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from django.contrib import messages
from .models import User

from models import *

# Create your views here.
def index(request):
    users = User.objects.all()
    return render(request, 'rest_users/index.html', {'users': users})

def add(request):
    users = User.objects.all()
    return render(request, 'rest_users/new.html', {'users': users})

def show(request, id):
    # users = User.objects.get(id=id)
    request.session['id'] = id
    return render(request, 'rest_users/show.html', {'users': User.objects.get(id=id)})

def edit(request, id):
    # users = User.objects.all()
    request.session['id'] = id
    return render(request, 'rest_users/edit.html', {'users': User.objects.get(id=id)})

def submit_add(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/new')
    else:
        User.objects.create(first_name=request.POST['first_name'],
                            last_name=request.POST['last_name'],
                            email_address=request.POST['email_address'],
                            )
        print "Successfully added ", request.POST['email_address'], " to the database."
        return redirect('/users')

def submit_edit(request, id):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/new')
    else:
        user = User.objects.get(id=id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email_address = request.POST['email_address']
        user.save()

        print "Successfully updated ", request.POST['email_address'], " in the database."
        return redirect('/users')

def submit_delete(request, id):
    request.session['id'] = id
    user = User.objects.get(id=id)
    user.delete()

    print "Successfully deleted ", user.email_address, " from the database."
    return redirect('/users')

    #     user = User.objects.get(id = id)
    #     user.first_name = request.POST['first_name']
    #     user.last_name = request.POST['last_name']
    #     user.email_address = request.POST['email_address']
    #     user.save()
    #     print "Successfully added ", request.POST['email_address'], " to the database."
    #     return redirect('/users')
    #
    # return render(request, 'survey_form/index.html')

# def submit(request):
#     print "Got POST info"
#
#     if len(request.POST['name']) < 1:
#         messages.warning(request, 'Name cannot be blank.')
#         print "Name cannot be blank!"
#     elif len(request.POST['comment']) < 1:
#         messages.warning(request, 'Comment cannot be blank!')
#         print "Comment cannot be blank!"
#     elif len(request.POST['comment']) > 120:
#         messages.warning(request, 'Comment cannot be more than 120 characters.')
#         print "Comment cannot be more than 120 characters."
#     else:
#         messages.success(request, 'Your information was submitted successfully!')
#         print "Success!"
#
#     request.session['name'] = request.POST['name']
#     request.session['location'] = request.POST['location']
#     request.session['language'] = request.POST['language']
#     request.session['comment'] = request.POST['comment']
#
#     return redirect('/result')
#
# def result(request):
#     return render(request, 'survey_form/result.html')
#
# def reset(request):
#     print "You have logged out and cleared the session."
#     session.clear()
#     return redirect('/')
