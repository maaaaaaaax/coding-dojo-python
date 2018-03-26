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
    return render(request, 'belt_reviewer/index.html', context)


def books(request):
    users = User.objects.all()
    authors = Author.objects.all()
    books = Book.objects.all()
    reviews = Review.objects.all()
    return render(request, 'belt_reviewer/books.html', {'users': users, 'authors': authors, 'books': books, 'reviews': reviews})


def add(request):
    if request.POST:
        context = {
            'old_form': request.POST
        }
    else:
        context = {
            'old_form': None
        }
    authors = Author.objects.all()
    return render(request, 'belt_reviewer/add.html', {'authors': authors})


def submit_review(request):
    if request.POST:
        context = {
            'old_form': request.POST
        }
    else:
        context = {
            'old_form': None
        }
    # # error checking for form submission
    errors = Author.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/books/add')

    # if the new author is not in your database, create a new book record before creating review

    if len(request.POST['new_author']) > 0:
        query = Author.objects.filter(name=request.POST['new_author'])
        if not query:
            print "Adding {} as a new author to our database.".format(request.POST['new_author'])
            Author.objects.create(name=request.POST['new_author'])

    # if the book is not in your database, create a new book record before creating review

    query = Book.objects.filter(title=request.POST['title'])
    if not query:
        print "Adding {} as a new book to our database.".format(request.POST['title'])
        Book.objects.create(title=request.POST['title'], author=Author.objects.get(name=request.POST['author']))

    Review.objects.create(description=request.POST['description'], stars=request.POST['stars'], book=Book.objects.get(title=request.POST['title']), user=User.objects.get(id=request.session['id']))

    return redirect('/books/')


def add_review (request):
	description = request.POST['description']
	stars = request.POST['stars']
	book = Book.objects.get(id=request.session['book_id'])
	user = User.objects.get(id=request.session['id'])
	Review.objects.create(user=user, book=book, stars=stars, description=description)
	return redirect ('/books/'+str(request.session['book_id']))


def delete(request, id):
	x = Review.objects.get(id=id)
	x.delete()
	return redirect ('/books/'+str(request.session['book_id']))


def user_profile(request, id):
	if 'id' in request.session:
		context	= {
			'user': User.objects.get(id=id),
			'reviews': Review.objects.filter(user=User.objects.get(id=id))
		}
		return render(request, 'belt_reviewer/user.html', context)
	else:
		return redirect('/')


# def specific(request, id):
#     if request.POST:
#         context = {
#             'old_form': request.POST
#         }
#     else:
#         context = {
#             'old_form': None
#         }
#     book = Book.objects.filter(id=id)
#     return render(request, 'belt_reviewer/specific.html', {'book': book})


def specific(request, id):
	request.session['book_id'] = id
	if 'id' in request.session:
		context = {
			'book_title': Book.objects.get(id=request.session['book_id']).title,
			'book_author': Book.objects.get(id=request.session['book_id']).author.name,
			'reviews': Review.objects.filter(book=Book.objects.get(id=request.session['book_id'])),
			'user': request.session['id'],
			'book': request.session['book_id']
		}
		return render(request, 'belt_reviewer/specific.html', context)
	else:
		return redirect('/')



def logout(request):
    print "Logged out and cleared session."
    request.session.clear()
    return redirect('/')



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
        request.session['id'] = User.objects.get(email=request.session['email']).id
        print "Welcome, ", request.session['first_name'], ". Your user id is ", request.session['id']
        request.session['source'] = "sign_up"
        return redirect('/books')



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
        print "Found request.session['email'] in database: {}".format(request.session['email'])
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
            request.session['id'] = User.objects.get(email=request.session['email']).id
            print "Welcome back, ", request.session['first_name'], ". Your user id is ", request.session['id']
            return redirect('/books')
