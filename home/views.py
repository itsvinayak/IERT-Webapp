from django.shortcuts import render
from .forms import message_from_about_us_form
from .models import *
from extra_links.models import *

def index(request):
    notices = notice_board.objects.order_by('-date')[:3]
    page_details={
                   "title":"IERT, Prayagraj",
                   "notice":notices
    }
    return render(request,"home/index.html",page_details)

def about_us(request):
    page_details={
                  "title":"about_us"
    }
    return render(request,"home/about_us.html",page_details)
def administration(request):
    page_details={
                  "title":"administration"
    }
    return render(request,"home/administration.html",page_details)

def vision_and_mission(request):
    page_details={
                  "title":"Vision and Mission"
    }
    return render(request,"home/vision_and_mission.html",page_details)

def academic_cal(request):
    page_details={
                  "title":"Academics Calender"
    }
    return render(request,"home/academics_calender.html",page_details)

def u_g_program(request):
    page_details={
                  "title":"U G Program"
    }
    return render(request,"home/u_g_program.html",page_details)


def about_city(request):
    page_details={
                  "title":"About City"
    }
    return render(request,"home/about_city.html",page_details)

def photo_gallery(request):
    images=gallery_pic.objects.all()
    page_details={
                  "images":images,
                  "title":"Photo Gallery"
    }
    return render(request,"home/photo_gallery.html",page_details)

def video_gallery(request):
    page_details={
                  "title":"video_gallery"
    }
    return render(request,"home/video_gallery.html",page_details)

def institution_holiday(request):
    holidays=holiday.objects.all()
    page_details={
                  "title":"institution_holiday",
                  "holiday":holidays
    }
    return render(request,"home/instiute_holiday.html",page_details)


def contact_us(request):
    if request.method=='POST':
            form=message_from_about_us_form(request.POST)
            form.save()

    form=message_from_about_us_form()
    page_details={
                  "title":"Contact Us",
                  "form":form
    }
    return render(request,"home/contact_us.html",page_details)

## Degree Division

def Computer_science_and_engg(request):
    cse=degree_detail.objects.all()
    for i in cse:
        if i.branch == "Computer science and engg":
            bd={
                 "title":i.branch,
                 "branch":i.branch,
                 "info":i.branch_imformation,
                 "vision":i.branch_vision,
                 "mission":i.branch_mission,
                 "table":i.timetable,
             }
    return render(request,"home/degree_division.html",bd)


def Electronics_engg(request):
    ee=degree_detail.objects.all()
    for i in ee:
        if i.branch == "Electronics_engg":
            bd={
                 "title":i.branch,
                 "branch":i.branch,
                 "info":i.branch_imformation,
                 "vision":i.branch_vision,
                 "mission":i.branch_mission,
            }
    return render(request,"home/degree_division.html",bd)


def Industrial_and_production_engg(request):
    ip=degree_detail.objects.all()
    for i in ip:
        if i.branch == "Industrial_and_production_engg":
            bd={
                 "title":i.branch,
                 "branch":i.branch,
                 "info":i.branch_imformation,
                 "vision":i.branch_vision,
                 "mission":i.branch_mission,
            }
    return render(request,"home/degree_division.html",bd)


def Instrumentation_and_Control_Engg(request):
    ice=degree_detail.objects.all()
    for i in ice:
        if i.branch == "Instrumentation_and_Control_Engg":
            bd={
                 "title":i.branch,
                 "branch":i.branch,
                 "info":i.branch_imformation,
                 "vision":i.branch_vision,
                 "mission":i.branch_mission,
                 }
    return render(request,"home/degree_division.html",bd)



def Civil_Engg(request):
    ce=degree_detail.objects.all()
    for i in ce:
        if i.branch == "Civil_Engg":
            bd={
                 "title":i.branch,
                 "branch":i.branch,
                 "info":i.branch_imformation,
                 "vision":i.branch_vision,
                 "mission":i.branch_mission,
            }
    return render(request,"home/degree_division.html",bd)



def Electrical_Engg(request):
    ene=degree_detail.objects.all()
    for i in ene:
        if i.branch == "Electrical_Engg":
            bd={
                 "title":i.branch,
                 "branch":i.branch,
                 "info":i.branch_imformation,
                 "vision":i.branch_vision,
                 "mission":i.branch_mission,
            }
    return render(request,"home/degree_division.html",bd)



def Mechanical_engg(request):
    me=degree_detail.objects.all()
    for i in me:
        if i.branch == "Mechanical_engg":
            bd={
                 "title":i.branch,
                 "branch":i.branch,
                 "info":i.branch_imformation,
                 "vision":i.branch_vision,
                 "mission":i.branch_mission,
            }
    return render(request,"home/degree_division.html",bd)


def Applied_science_and_humanity(request):
    ash=degree_detail.objects.all()
    for i in ash:
        if i.branch == "Applied_science_and_humanity":
            bd={
                 "title":i.branch,
                 "branch":i.branch,
                 "info":i.branch_imformation,
                 "vision":i.branch_vision,
                 "mission":i.branch_mission,
            }
    return render(request,"home/degree_division.html",bd)


def Management(request):
    m=degree_detail.objects.all()
    for i in m:
        if i.branch == "Management":
            bd={
                 "title":i.branch,
                 "branch":i.branch,
                 "info":i.branch_imformation,
                 "vision":i.branch_vision,
                 "mission":i.branch_mission,
            }
    return render(request,"home/degree_division.html",bd)



## Library

def Central_Library(request):
    page_details={
        "title":"Central Library"
    }
    return render(request,"home/Central_Library.html",page_details)


def Reference_Library(request):
    page_details={
        "title":"Reference Library"
    }
    return render(request,"home/Reference_Library.html",page_details)


###########################################


def Health_Center(request):
    page_details={
                 "title":" Health Center",
    }
    return render(request,"home/health_care.html",page_details)

def Hostels(request):
    page_details={
                    "title":"Hostels"
    }
    return render(request,"home/Hostels.html",page_details)


def Banking(request):
    page_details={
                    "title":"Banking"
    }
    return render(request,"home/banking.html",page_details)
