from django.urls import path, include
from . import views

urlpatterns = [
          path('',views.diploma_staff,name='diploma_staff'),
]
