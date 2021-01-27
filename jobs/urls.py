from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = "home"),
    path('signup/', views.SignUpView.as_view(), name = "signup"),
    path('ajax/validate_username/', views.validate_username, name='validate_username'),
    path("<int:job_id>/", views.jobs, name="job"),
    path("<int:job_id>/add_job_comment", views.add_job_comment, name="add_job_comment"),
]