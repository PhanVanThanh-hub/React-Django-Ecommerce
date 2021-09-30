from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('register.api.urls')),
]