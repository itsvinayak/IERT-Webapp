from django.db import models


class message_from_about_us(models.Model):
    topic=models.CharField(max_length=200)
    text=models.TextField()
    def __str__(self):
        return self.topic


class degree_detail(models.Model):
    branch=models.CharField(max_length=300)
    branch_imformation=models.TextField()
    timetable=models.TextField()
    branch_vision=models.TextField()
    branch_mission=models.TextField()
    def __str__(self):
        return self.branch

class gallery_pic(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="gallery/")
    def __str__ (self):
        return self.title
