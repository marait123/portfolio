from django.db import models
from datetime import datetime
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
    
class comment(models.Model):
    blog_id = models.ForeignKey(blog, on_delete=models.CASCADE)
    body = models.TextField()
    user_name = models.CharField(max_length=200)
    email = models.EmailField()
    date = models.DateTimeField(default = datetime.now)

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.summary()