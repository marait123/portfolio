from django.contrib import admin
from .models import Job, JobComment
from .models import Interests

# Register your models here.
admin.site.register(Job)
admin.site.register(JobComment)
admin.site.register(Interests)
