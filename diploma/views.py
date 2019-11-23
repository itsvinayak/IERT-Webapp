from django.shortcuts import render
from .models import diploma_facultys


def diploma_staff(request):
    data = diploma_facultys.objects.all()
    page_details = {"title": "Diploma Facultys", "data": data}
    return render(request, "diploma/diploma_facultys.html", page_details)
