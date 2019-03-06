from django.db import models


class message_from_about_us(models.Model):
    topic=models.CharField(max_length=200)
    text=models.TextField()
    def __str__(self):
        return self.topic

class degree_detail(models.Model):
    branch=models.CharField(max_length=300)
    branch_imformation=models.TextField()
    timetable_1_year=models.TextField()
    timetable_2_year=models.TextField()
    timetable_3_year=models.TextField()
    timetable_4_year=models.TextField()
    branch_vision=models.TextField()
    branch_mission=models.TextField()
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
