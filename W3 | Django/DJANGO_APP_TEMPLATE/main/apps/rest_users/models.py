# Inside models.py
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be more than 1 characters"
        if len(postData['last_name']) < 2:
            errors["first_name"] = "Last name should be more than 1 characters"
        if len(postData['email_address']) < 4:
            errors["email"] = "Email should be more than 10 characters"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    # age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    # updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
