from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = "home"),
    path("<int:job_id>/", views.jobs, name="job"),
]