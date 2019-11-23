from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from user import views as user
from home import views as myapp_views
from django.contrib.auth import views as auth


############# admin #########################
from django.contrib import admin

## in case you need a different diploma panel
# from diploma.admin import diploma_admin_site
#############################################


###for error 404 ##################
from django.conf.urls import handler404, handler500

###################################

################admin setting####################
admin.site.site_header = "iert admin"
admin.site.site_title = "iert admin"
# admin.site.site_url = 'http://coffeehouse.com/'
admin.site.index_title = "Welcome IERT Administration"
admin.empty_value_display = "**Empty**"

################################################


urlpatterns = [
    # extra pages in body ___
    path("extra_links/", include("extra_links.urls")),
    # side bar links___
    path("aside/", include("aside.urls")),
    #############################################
    path("news/", include("iert_news.urls")),
    path("", include("home.urls")),
    ########################diploma ###########
    path("diploma/", include("diploma.urls")),
    #######################pwa app url#####################
    ###leave it empty it always run#######################
    path("", include("pwa.urls")),
    ###################password reset###############
    path(
        "password_reset/",
        auth.PasswordResetView.as_view(template_name="user/password_reset.html"),
        name="password_reset",
    ),
    path(
        "password_reset/done",
        auth.PasswordResetDoneView.as_view(
            template_name="user/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        auth.PasswordResetConfirmView.as_view(
            template_name="user/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete/",
        auth.PasswordResetCompleteView.as_view(
            template_name="user/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    #####user related path##########################
    path("user/", include("user.urls")),
    path("login/", user.Login, name="login"),
    path(
        "logout/",
        auth.LogoutView.as_view(template_name="home/index.html"),
        name="logout",
    ),
    path("register/", user.register, name="register"),
    path("profile/", user.Profile, name="profile"),
    path("Profile_update/", user.Profile_update, name="Profile_update"),
    # admin path
    path("admin/", admin.site.urls),
    # in case you need different admin panel for diploma
    # path('diploma-admin/',diploma_admin_site.urls),
    # add style to admin by uncomment
    # path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


##error 404 ####
handler404 = myapp_views.error_404
handler500 = myapp_views.error_500
