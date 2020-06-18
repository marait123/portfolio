from django.db import models

# Create your models here.

class blog(models.Model):
    image = models.ImageField(upload_to="images/",default = '../portfolio/static/mohammed.jpg')
    #summary = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    body = models.TextField()
    pubDate = models.DateTimeField()


    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title
    
