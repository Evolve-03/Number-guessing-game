from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit-guess', views.submit_guess, name='submit_guess'),
]