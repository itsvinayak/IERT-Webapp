from django.shortcuts import render, get_object_or_404, redirect
from .models import new, Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import user_news_story, CommentForm
from django.contrib.auth.models import User


def index(request):
    n = new.objects.order_by("-date")[:6]
    if request.method == "POST":
        form = user_news_story(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = user_news_story()

    ##################like button################
    if_dic = []
    for i in n:
        if i.likes.filter(id=request.user.id).exists():
            if_dic.append(i.id)
        news = get_object_or_404(new, id=i.id)
        i.no_of_comment = Comment.objects.filter(news=news).count()

    ##############################################

    page_details = {"title": "news in iert", "news": n, "form": form, "if_dic": if_dic}
    return render(request, "iert_news/news_index.html", page_details)


def like_news(request):
    news = get_object_or_404(new, id=request.POST.get("news_id"))
    is_liked = False
    try:
        if news.likes.filter(id=request.user.id).exists():
            news.likes.remove(request.user)
            is_liked = False
        else:
            news.likes.add(request.user)
            is_liked = True
    except:
        messages.info(request, f"log in to like post")
    return redirect("news")


##############new_comments#########################


def new_comments(request, id):
    news = get_object_or_404(new, id=id)
    com = Comment.objects.filter(news=news, reply=None).order_by("-id")
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            content = request.POST.get("content")
            reply_id = request.POST.get("comment_id")
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            print(comment_qs)
            comment = Comment.objects.create(
                news=news, user=request.user, content=content, reply=comment_qs
            )
            comment.save()
            return redirect("new_comments", id=id)

    form = CommentForm()
    page_details = {"title": "comments", "com": com, "news": news, "form": form}
    return render(request, "iert_news/comments.html", page_details)
