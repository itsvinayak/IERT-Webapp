from django.shortcuts import render
from .forms import message_from_about_us_form
from .models import *
from extra_links.models import *
from aside.models import *

def index(request):
    notices = notice_board.objects.order_by('-date')[:]
    popup_notice=popup.objects.all()
    page_details={
                   "title":"IERT, Prayagraj",
                   "popup_notice":popup_notice,
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
                  "title":"Vision and Mission",
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
    a='Computer Science & Engineering'
    teacher = facultys.objects.all().filter(branch=a)
    notices = notice_board.objects.filter(branch=a)
    bra = degree_detail.objects.filter(branch='Computer Science & Engineering')
    bd={
         "title":"Computer science and engg",
         "notice":notices,
         "teacher":teacher,
         "bra":bra,
    }
    return render(request,"home/degree_division.html",bd)


def Electronics_engg(request):
    a='Electronic Engineering'
    teacher = facultys.objects.all().filter(branch=a)
    notices = notice_board.objects.filter(branch=a)
    bra = degree_detail.objects.filter(branch='Electronic Engineering')
    bd={
         "title":"Electronics_engg",
         "notice":notices,
         "teacher":teacher,
         "bra":bra,
    }
    return render(request,"home/degree_division.html",bd)


def Industrial_and_production_engg(request):
    a='Industrial & Production Engineering'
    teacher = facultys.objects.all().filter(branch=a)
    notices = notice_board.objects.filter(branch=a)
    bra = degree_detail.objects.filter(branch='Industrial & Production Engineering')
    bd={
         "title":"Industrial and production engg",
         "notice":notices,
         "teacher":teacher,
         "bra":bra,
    }
    return render(request,"home/degree_division.html",bd)


def Instrumentation_and_Control_Engg(request):
    a='Instrumentation and Control Engineering'
    teacher = facultys.objects.all().filter(branch=a)
    notices = notice_board.objects.filter(branch=a)
    bra = degree_detail.objects.filter(branch='Instrumentation & Control Engineering')
    bd={
         "title":"Instrumentation and Control Engg",
         "notice":notices,
         "teacher":teacher,
         "bra":bra,
    }
    return render(request,"home/degree_division.html",bd)



def Civil_Engg(request):
    a='Civil Engineering'
    teacher = facultys.objects.all().filter(branch=a)
    notices = notice_board.objects.filter(branch=a)
    bra = degree_detail.objects.filter(branch='Civil Engineering')
    bd={
         "title":"Civil Engg",
         "notice":notices,
         "teacher":teacher,
         "bra":bra,
    }
    return render(request,"home/degree_division.html",bd)



def Electrical_Engg(request):
    a='Electrical Engineering'
    teacher = facultys.objects.all().filter(branch=a)
    notices = notice_board.objects.filter(branch=a)
    bra = degree_detail.objects.filter(branch='Electrical Engineering')
    bd={
         "title":"Electrical Engg",
         "notice":notices,
         "teacher":teacher,
         "bra":bra,
    }
    return render(request,"home/degree_division.html",bd)



def Mechanical_engg(request):
    a='Mechanical Engineering'
    teacher = facultys.objects.all().filter(branch=a)
    notices = notice_board.objects.filter(branch=a)
    bra = degree_detail.objects.filter(branch='	Mechanical Engineering')
    bd={
         "title":"Mechanical engg",
         "notice":notices,
         "teacher":teacher,
         "bra":bra,
    }
    return render(request,"home/degree_division.html",bd)


def Applied_science_and_humanity(request):
    a='Applied Science and Humanity'
    teacher = facultys.objects.all().filter(branch=a)
    notices = notice_board.objects.filter(branch=a)
    bra = degree_detail.objects.filter(branch='Applied Science and Humanity')
    bd={
         "title":"Applied science and humanity",
         "notice":notices,
         "teacher":teacher,
         "bra":bra,
    }
    return render(request,"home/degree_division.html",bd)


def Management(request):
    a='Management'
    teacher = facultys.objects.all().filter(branch=a)
    notices = notice_board.objects.filter(branch=a)
    bra = degree_detail.objects.filter(branch='	Management')
    bd={
         "title":"Management",
         "notice":notices,
         "teacher":teacher,
         "bra":bra,
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


###########error 404 ################


def error_404(request,*kwags):
        data = {}
        return render(request,'home/error_404.html', data)

def error_500(request,*kwags):
        data = {}
        return render(request,'home/error_500.html', data)

#################################################################
