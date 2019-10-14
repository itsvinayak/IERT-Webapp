from django.shortcuts import render
from .models import facultys,recruitment_notice,download_link

def faculty(request):
    fac=facultys.objects.all()
    l=recruitment_notice.objects.all()

    page_details={
        "title" : "faculty",
        "notice": l,
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
    teacher=facultys.objects.all().filter(Designation='Computer_science_and_engg')
    page_details={
         "title":"computer_center",
         "teachers":teacher,
    }
    return render(request,"aside/computer_center.html",page_details)

def placement(request):
    page_details={
         "title":"placements",
    }
    return render(request,"aside/placement.html",page_details)


def recruitment(request):
    l=recruitment_notice.objects.all()
    page_details={
         "li":l,
         "title":"recruitment"
    }
    return render(request,"aside/recruitment.html",page_details)

def technovation(request):
    page_details={
         "title":"Technovation"
    }
    return render(request,"aside/technovation.html",page_details)

def Udbhav(request):
    page_details={
         "title":"Udbhav"
    }
    return render(request,"aside/Udbhav.html",page_details)

def Achievements(request):
    page_details={
         "title":"Achievements"
    }
    return render(request,"aside/Achievements.html",page_details)

def Women_Grievance_Cell(request):
    page_details={
             "title":"Women Grievance Cell"
        }
    return render(request,"aside/Women_Grievance_Cell.html",page_details)


def rti(request):
    page_details={
        "title":"RTI"
    }
    return render(request,"aside/rti.html",page_details)

def internship(request):
    page_details={
        "title":"internship"
    }
    return render(request,"aside/internship.html",page_details)
