from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = "home"),
   # path("<int:blog_id>/", views.details, name="details"),
]