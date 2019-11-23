from django.contrib import admin
from .models import notice_board
from home.models import popup

admin.site.register(notice_board)
admin.site.register(popup)
