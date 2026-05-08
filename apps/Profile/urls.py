from django.urls import path
from . import views

urlpatterns = [
    path('edit/', views.edit_profile_view, name='edit_profile'),
    path('', views.profile_view, name='profile'),  # my profile (no username needed)
    path('<str:username>/', views.profile_view, name='profile_view'),  # view other profile
]