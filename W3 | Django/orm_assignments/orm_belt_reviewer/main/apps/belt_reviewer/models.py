
# Inside models.py
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # if len(postData['first_name']) < 2:
        #     errors["first_name"] = "First name should be more than 1 characters"
        # if len(postData['last_name']) < 2:
        #     errors["first_name"] = "Last name should be more than 1 characters"
        # if len(postData['email_address']) < 4:
        #     errors["email"] = "Email should be more than 10 characters"
        # first_name should be letters only, at least 2 characters and that it was submitted
        if len(postData['first_name']) < 2 or postData['first_name'].isalpha() is not True:
            # flash("First name cannot be less than 2 characters and must be alphabetical.")
            errors["first_name"] = "First name should be more than 1 character."
            print "First name cannot be less than 2 characters and must be alphabetical."
        # last_name should be letters only, at least 2 characters and that it was submitted
        if len(postData['last_name']) < 2 or postData['last_name'].isalpha() is not True:
            # flash("Last name cannot be less than 2 characters and must be alphabetical.")
            errors["last_name"] = "Last name should be more than 1 character."
            print "Last name cannot be less than 2 characters and must be alphabetical."
        # email should be letters only, at least 2 characters and that it was submitted
        if len(postData['email']) < 1:
            # flash("Email cannot be blank!")
            errors["email"] = "Email cannot be blank."
            print "Email cannot be blank!"
        # check if the user provided email is already in the database
        query = User.objects.filter(email=postData['email'])
        if query:
            errors["email_in_use"] = "This email is already in use."
            print "We already have this email in our database."
        if len(postData['password']) < 6 or postData['password'] != postData['password_confirm']:
            # flash("Passwords must be at least 6 characters and must match.")
            errors["password"] = "Passwords must be at least 6 characters and must match."
            print "Passwords must be at least 6 characters and must match."
        return errors

class AuthorManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # if user provided a new author, check them against the DB
        if len(postData['new_author']) > 0:
            # check if the user provided author is already in the database
            query = Author.objects.filter(name=postData['new_author'])
            if query:
                errors["repeat_author"] = "This author is already in our database. Please select this author from the dropdown menu."
                print "This author is already in our database. Please select this author from the dropdown menu."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # usernames must start with '@' character
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = AuthorManager()

class Book(models.Model):
    title = models.CharField(max_length=255)
    # There can be many books to one author
    author = models.ForeignKey(Author, related_name = "books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Review(models.Model):
    description = models.CharField(max_length=255)
    stars = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # There can be many reviews to one book
    book = models.ForeignKey(Book, related_name = "reviews")
    # There can be many reviews to one user
    user = models.ForeignKey(User, related_name = "reviews")
