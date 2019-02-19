from django.shortcuts import render
from .models import book


def index(request):
    books=book.objects.all()
    page_details={
                    "books":books,
                    "title":"books",

    }
    return render(request,'books/book.html',page_details)
