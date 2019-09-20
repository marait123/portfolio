from django.shortcuts import render
from datetime import date

from .models import Job
# Create your views here.
def home(request):
    today = date.today()
    year = today.year

    jobs = Job.objects
    return render(request,'jobs/home.html',{'year':year,'jobs':jobs})