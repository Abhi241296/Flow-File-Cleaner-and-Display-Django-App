from django.urls import path
from . import views

urlpatterns = [
    path('cleanfiles', views.CleanedData, name='cleanfiles')
]