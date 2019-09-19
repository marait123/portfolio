from django.shortcuts import render
from datetime import date

# Create your views here.
def home(request):
    today = date.today()
    year = today.year

    return render(request,'jobs/home.html',{'year':year})