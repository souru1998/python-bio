from django.db import models

# Create your models here.

class contacttable(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=200)

class registrationtable(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    re_password = models.CharField(max_length=200)