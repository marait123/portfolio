from django.shortcuts import render
from datetime import date

from .models import Job
from .models import Interests
# Create your views here.
def home(request):
    today = date.today()
    year = today.year

    jobs = Job.objects
    interests = Interests.objects
    return render(request,'jobs/home.html',{'year':year,'jobs':jobs, 'interests':interests})