from django.shortcuts import render,get_object_or_404,redirect
from .models import new
from django.contrib import messages
from .forms import user_news_story


def index(request):
    n=new.objects.order_by('-date')[:6]
    if request.method=='POST':
            form=user_news_story(request.POST,request.FILES)
            if form.is_valid():
                form.save()
    form=user_news_story(request.POST)

##################like button################
    if_dic=[]
    for i in n:
        if i.likes.filter(id=request.user.id).exists():
            if_dic.append(i.id)
##############################################

    page_details={
                    "title":"news in iert",
                    "news":n,
                    "form":form,
                    "if_dic":if_dic
    }
    return render(request,"iert_news/news_index.html",page_details)

def like_news(request):
    news = get_object_or_404(new,id=request.POST.get('news_id'))
    is_liked = False
    try:
        if news.likes.filter(id=request.user.id).exists():
            news.likes.remove(request.user)
            is_liked = False
        else:
            news.likes.add(request.user)
            is_liked = True
    except:
        messages.info(request, f'log in to like post')
    return redirect("news")
