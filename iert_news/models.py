from django.db import models
from django.contrib.auth.models import User

class new(models.Model):
    title=models.CharField(max_length=300)
    author=models.CharField(max_length=300)
    date=models.DateField(null=True,blank=True)
    likes=models.ManyToManyField(User,related_name="likes",blank=True)
    image=models.ImageField(null=True,blank=True,upload_to='media/')
    info=models.TextField()
    def __str__(self):
        return self.title


class new_by_viewer(models.Model):
    title=models.CharField(max_length=300)
    author=models.CharField(max_length=300)
    date=models.DateField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True,upload_to='media/')
    info=models.TextField()
    def __str__(self):
        return self.title
