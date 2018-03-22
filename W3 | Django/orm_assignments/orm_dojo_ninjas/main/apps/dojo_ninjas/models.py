# Inside models.py
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo_id = models.ForeignKey(Dojo, related_name = "ninjas")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

# Shell command to create a new student:
# >>> Ninja.objects.create(first_name="Max",last_name="Wiederholt",dojo_id=Dojo.objects.get(id=1))

# Shell command to print the name of the Dojo of a specific student
# >>> Ninja.objects.get(id=1).dojo_id.name

# Shell command to print the first name of a student of a specific Dojo
# Dojo.objects.first().ninjas.all()[0].first_name
