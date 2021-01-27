from django.db import models
from datetime import datetime
# Create your models here.

class Job(models.Model):
    type_choices = (('H','Hardware'), ('S','Software'))
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=100, default= 'title default')
    body = models.TextField(default= 'body default')
    date = models.DateTimeField(default = datetime.now)
    job_type = models.CharField(max_length=1, default = 'S', choices=type_choices)
    def summary(self):
        if len(self.body) > 100:
            return self.body[:100]
        else:
            return self.body

    def __str__(self):
        return self.title
class Interests(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=100, default= 'title default')
    summary = models.TextField(default= 'title default')
    def __str__(self):
        return self.title


class JobComment(models.Model):
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    body = models.TextField()
    user_name = models.CharField(max_length=200)
    email = models.EmailField()
    date = models.DateTimeField(default = datetime.now)

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.summary()