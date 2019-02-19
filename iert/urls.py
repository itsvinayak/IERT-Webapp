"""iert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from user import views as user
from django.contrib.auth import views as auth
from books import views as books

urlpatterns = [

    #extra pages in body ___
    path('extra_links/',include('extra_links.urls')),

    #side bar links___
    path('aside/',include('aside.urls')),

    #############################################
    path('news/',include('iert_news.urls')),
    path('books/',books.index,name='books'),
    path('',include('home.urls')),


    #user related path
    path('user/',include('user.urls')),
    path('login/',user.Login,name='login'),
    path('logout/',auth.LogoutView.as_view(template_name='home/index.html'),name='logout'),
    path('register/',user.register,name='register'),
    path('profile/',user.Profile,name='profile'),
    path('Profile_update/', user.Profile_update, name='Profile_update'),

    #admin path
    path('admin/',admin.site.urls),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
