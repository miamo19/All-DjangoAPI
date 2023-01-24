#from django
from django.urls import path

#from project
from . import views

urlpatterns = [
    path('', views.api_home),
]
