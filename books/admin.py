from django.contrib import admin
from .models import book,books_by_user

# Register your models here.
admin.site.register(book)
admin.site.register(books_by_user)
