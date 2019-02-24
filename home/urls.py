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

from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('about_us',views.about_us,name='about_us'),
    path('about_city',views.about_city,name='about_city'),
    path('photo_gallery',views.photo_gallery,name='photo_gallery'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('academic_cal',views.academic_cal,name='academic_cal'),
    path('u_g_program',views.u_g_program,name='u_g_program'),
    path('vision_and_mission',views.vision_and_mission,name='vision_and_mission'),
    path('administration',views.administration,name='administration'),
    path('video_gallery',views.video_gallery,name='video_gallery'),
    path('institution_holiday',views.institution_holiday,name='institution_holiday'),
    path('Computer_science_and_engg',views.Computer_science_and_engg,name='Computer_science_and_engg'),
    path('Electronics_engg',views.Electronics_engg,name='Electronics_engg'),
    path('Industrial_&_production_engg',views.Industrial_and_production_engg,name='Industrial_&_production_engg'),
    path('Instrumentation_&_Control_Engg',views.Instrumentation_and_Control_Engg,name='Instrumentation_&_Control_Engg'),
    path('Civil_Engg',views.Civil_Engg,name='Civil_Engg'),
    path('Electrical_Engg',views.Electrical_Engg,name='Electrical_Engg'),
    path('Mechanical_engg',views.Mechanical_engg,name='Mechanical_engg'),
    path('Applied_science_and_humanity',views.Applied_science_and_humanity,name='Applied_science_and_humanity'),
    path('Management',views.Management,name='Management'),
    path('Central_Library',views.Central_Library,name="Central_Library"),
    path('Reference_Library',views.Reference_Library,name="Reference_Library"),
    path('Health_Center',views.Health_Center,name="Health_Center"),
    path('Hostels',views.Hostels,name="Hostels"),
    path('Banking',views.Banking,name="Banking"),

]
