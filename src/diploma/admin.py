from django.contrib import admin
from .models import diploma_facultys

# in case of different admin panel
#####################################################
# from django.contrib.admin import AdminSite
#
# class DiplomaAdminSite(AdminSite):
#     site_header = "IERT DIPLOMA ADMIN"
#     site_title = "IERT DIPLOMA ADMIN"
#     index_title = "Welcome to IERT Diploma Admin Portal"
#
# diploma_admin_site = DiplomaAdminSite(name='iert_diploma_admin')
########################################################################

admin.site.register(diploma_facultys)
