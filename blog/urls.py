from . import views
from django.urls import path

urlpatterns = [
    path('', views.allblogs, name = "allblogs"),
    path("<int:blog_id>/", views.details, name="details"),
]