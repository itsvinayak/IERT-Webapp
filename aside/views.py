from django.shortcuts import render
from .models import facultys

def faculty(request):
    fac=facultys.objects.all()

    page_details={
        "title" : "faculty",
        "fac" : fac
    }
    return render(request,"aside/faculty.html",page_details)

def anti_ragging(request):
    page_details={
         "title":"anti_ragging"
    }
    return render(request,"aside/anti_ragging.html")

def recruitment(request):
    page_details={
         "title":"recruitment"
    }
    return render(request,"aside/recruitment.html")

def rti(request):
    page_details={
        "title":"rti"
    }
    return render(request,"aside/rti.html")
