# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pet(models.Model):
    pet_name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    weight_in_pounds = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.pet_name

class Appointment(models.Model):
    date_of_appointment = models.DateField()
    duration_minutes = models.IntegerField()
    special_instructions = models.CharField(max_length=100)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
