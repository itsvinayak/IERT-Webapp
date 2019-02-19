from django.db import models

class new(models.Model):
    title=models.CharField(max_length=300)
    author=models.CharField(max_length=300)
    date=models.DateField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True,default='',upload_to='media/')
    info=models.TextField()
    def __str__(self):
        return self.title


class new_by_viewer(models.Model):
    title=models.CharField(max_length=300)
    author=models.CharField(max_length=300)
    date=models.DateField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True,default='',upload_to='media/')
    info=models.TextField()
    def __str__(self):
        return self.title
