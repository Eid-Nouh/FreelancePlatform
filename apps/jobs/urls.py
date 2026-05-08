from django.urls import path
from . import views

urlpatterns = [

    path('', views.find_jobs, name='find_jobs'),
    path('post/', views.post_job, name='post_job'),
    path('<int:id>/', views.job_details, name='job_details'),
    path('apply/<int:id>/', views.apply_job),
]