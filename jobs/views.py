from django.shortcuts import render, get_object_or_404
from datetime import date
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.core import serializers
from .models import Job, JobComment
from .models import Interests
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
# from django.core.mail import send_mail

# Create your views here.
def home(request):
    today = date.today()
    year = today.year
    jobs = Job.objects
    interests = Interests.objects
    return render(request,'jobs/home.html', {'year':year,'jobs':jobs, 'interests':interests})

def jobs(request, job_id):
    job = get_object_or_404(Job, pk = job_id)
    comments = JobComment.objects.filter(job_id = job_id).order_by('-date')
    return  render(request, 'jobs/job.html', {'job':job, 'comments':comments})

#TODO:  
# 1. store the comments 
# 2. check the validity of the passed data
# 3. check that the email exists
def add_job_comment(request:HttpRequest, job_id):
    print("email sent to , ", request.POST.get('email',None))

    try:
        print("email sent to , ", request.POST.get('email',None))
        # send_mail(
        #     'Subject here',
        #     'Here is the message.',
        #     'from@example.com',
        #     [request.POST.get('email',None)],
        #     fail_silently=False,
        # )
        objComment= JobComment.objects.create(job_id = Job.objects.get(pk=job_id), user_name =request.POST.get('comment_author',None), email = request.POST.get('email',None), body = request.POST.get('comment',None))
        print(type(objComment))
        return JsonResponse({'comment': serializers.serialize('json',[objComment]) }, status=200)
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)

        return JsonResponse({}, status=403)

class SignUpView(CreateView):
    template_name = 'jobs/signup.html'
    form_class = UserCreationForm
 
def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)