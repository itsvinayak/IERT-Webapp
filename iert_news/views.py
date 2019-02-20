from django.shortcuts import render
from .models import new
from .forms import user_news_story


def index(request):
    n=new.objects.order_by('-date')[:6]
    if request.method=='POST':
            form=user_news_story(request.POST,request.FILES)
            if form.is_valid():
                form.save()
    form=user_news_story(request.POST)

    page_details={
                    "title":"news in iert",
                    "news":n,
                    "form":form

    }

    return render(request,"iert_news/news_index.html",page_details)
