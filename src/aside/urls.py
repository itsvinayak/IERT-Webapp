"""iert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path("faculty", views.faculty, name="faculty"),
    path("anti_ragging", views.anti_ragging, name="anti_ragging"),
    path("internship", views.internship, name="internship"),
    path("computer_center", views.computer_center, name="computer_center"),
    path("download", views.download, name="download"),
    path("technovation", views.technovation, name="technovation"),
    path("placements", views.placement, name="placement"),
    path("Udbhav", views.Udbhav, name="Udbhav"),
    path("Achievements", views.Achievements, name="Achievements"),
    path(
        "Women_Grievance_Cell", views.Women_Grievance_Cell, name="Women_Grievance_Cell"
    ),
    path("recruitment", views.recruitment, name="recruitment"),
    path("rti", views.rti, name="rti"),
]
