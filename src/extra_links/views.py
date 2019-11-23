from django.shortcuts import render
from .models import notice_board


def notice_board_view(request):
    nb = notice_board.objects.order_by("-date")
    page_details = {"nb": nb, "title": "Notice Board"}
    return render(request, "extra_links/notice_board.html", page_details)


def desk(request):
    page_details = {"title": "desk"}
    return render(request, "extra_links/desk.html", page_details)


def director(request):
    page_details = {"title": "Director"}
    return render(request, "extra_links/director.html", page_details)


def notice(request, id):
    nb = notice_board.objects.get(id=id)
    page_details = {"nb": nb, "title": "Notice"}
    return render(request, "extra_links/notice_page.html", page_details)
