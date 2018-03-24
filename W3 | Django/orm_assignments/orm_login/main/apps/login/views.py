# Create your views here.

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from django.contrib import messages
import bcrypt

from .models import User
from models import *



# Create your views here.
def index(request):
    users = User.objects.all()
    if request.POST:
        context = {
            'users': users,
            'old_form': request.POST
        }
    else:
        context = {
            'users': users,
            'old_form': None
        }
    return render(request, 'login/index.html', context)



def success(request):
    users = User.objects.all()
    return render(request, 'login/success.html', {'users': users})



def logout(request):
    print "Logged out and cleared session."
    request.session.clear()
    return redirect("/")



def sign_up(request):
    users = User.objects.all()
    if request.POST:
        context = {
            'users': users,
            'old_form': request.POST
        }
    else:
        context = {
            'users': users,
            'old_form': None
        }
    # # error checking for form submission
    request.session['email'] = request.POST['email']
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        # create hashed password and salt
        hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        print "Hashed password: ", hashed_pw
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed_pw)
        request.session['email'] = User.objects.get(email=request.POST['email']).email
        request.session['first_name'] = User.objects.get(email=request.session['email']).first_name
        request.session['last_name'] = User.objects.get(email=request.session['email']).last_name
        print "Success! Created new user: ", request.session['email']
        print "Welcome, ", request.session['first_name']
        request.session['source'] = "sign_up"
        return redirect('/success')



def sign_in(request):
    users = User.objects.all()
    if request.POST:
        context = {
            'users': users,
            'old_form': request.POST
        }
    else:
        context = {
            'users': users,
            'old_form': None
        }
    # first_name should be letters only, at least 2 characters and that it was submitted
    if len(request.POST['email_sign_in']) < 1:
        # flash("First name cannot be less than 2 characters and must be alphabetical.")
        print "Email cannot be blank."
        return redirect('/')
    # check if the user provided email is already in the database
    request.session['email'] = request.POST['email_sign_in']
    query = User.objects.filter(email=request.session['email'])
    if not query:
        print "Your email and password do not match our records. Please try again."
        return redirect('/')
    else:
        print "New email: {}".format(request.session['email'])
        if request.POST['password_sign_in'] != request.POST['password_confirm_sign_in']:
            print "Password does not match password confirm. Please enter the same password twice."
            return redirect('/')
        # check user provided password against hashed password in database
        stored_pw = User.objects.get(email=request.session['email']).password
        if bcrypt.checkpw(request.POST['password_sign_in'].encode(), stored_pw.encode()) != True:
            print "Your email and password do not match our records. Please try again."
            return redirect('/')
        else:
            request.session['first_name'] = User.objects.get(email=request.session['email']).first_name
            request.session['last_name'] = User.objects.get(email=request.session['email']).last_name
            request.session['source'] = "sign_in"
            print "Welcome back, ", request.session['first_name']
            return redirect('/success')
