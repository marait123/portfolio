from django.shortcuts import render, get_object_or_404
from datetime import date

from .models import Job
from .models import Interests
# Create your views here.
def home(request):
    today = date.today()
    year = today.year

    jobs = Job.objects
    interests = Interests.objects
    return render(request,'jobs/home.html', {'year':year,'jobs':jobs, 'interests':interests})

def jobs(request, job_id):
    job = get_object_or_404(Job, pk = job_id)
    return  render(request, 'jobs/job.html', {'job':job})
 