from django.db import models


class book(models.Model):
    title=models.CharField(max_length=300)
    author=models.CharField(max_length=300)
    document=models.FileField(upload_to='document/')
    info=models.TextField()
    def __str__(self):
        return self.title


class books_by_user(models.Model):
    title=models.CharField(max_length=300)
    author=models.CharField(max_length=300)
    document=models.FileField(upload_to='document/')
    info=models.TextField()
    def __str__(self):
        return self.title
