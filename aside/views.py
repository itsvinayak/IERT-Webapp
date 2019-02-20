from django.shortcuts import render
from .models import facultys,recruitment_notice,download_link

def faculty(request):
    fac=facultys.objects.all()

    page_details={
        "title" : "faculty",
        "fac" : fac
    }
    return render(request,"aside/faculty.html",page_details)


def download(request):
    link=download_link.objects.all()
    page_details={
        "title" : "Download",
        "links" : link
    }
    return render(request,"aside/download.html",page_details)


def anti_ragging(request):
    page_details={
         "title":"anti_ragging"
    }
    return render(request,"aside/anti_ragging.html",page_details)

def computer_center(request):
    page_details={
         "title":"computer_center"
    }
    return render(request,"aside/computer_center.html",page_details)

def recruitment(request):
    l=recruitment_notice.objects.all()
    page_details={
         "li":l,
         "title":"recruitment"
    }
    return render(request,"aside/recruitment.html",page_details)

def rti(request):
    page_details={
        "title":"rti"
    }
    return render(request,"aside/rti.html")
