from django.db import models


class message_from_about_us(models.Model):
    topic=models.CharField(max_length=200)
    text=models.TextField()
    def __str__(self):
        return self.topic

class degree_detail(models.Model):
    branch=models.CharField(max_length=300)
    branch_imformation=models.TextField(null=True,blank=True)
    branch_vision=models.TextField(null=True,blank=True)
    branch_mission=models.TextField(null=True,blank=True)
    def __str__(self):
        return self.branch

class gallery_pic(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="gallery/")
    def __str__ (self):
        return self.title


class holiday(models.Model):
    holiday_html=models.TextField()
    def __str__(self):
        return self.holiday_html
