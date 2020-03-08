from django.db import models

# Create your models here.

class Job(models.Model):
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=200)

class Interests(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=200)