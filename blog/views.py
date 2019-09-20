from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def allblogs(request):
    return render(request,"blog/allblogs.htm")
    