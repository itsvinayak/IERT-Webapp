from django.db import models

class facultys(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(null=True,blank=True,default='profile_pics/default.jpg',upload_to='media/teachers_img/')
    Designation=models.CharField(max_length=400)
    Qualification=models.CharField(max_length=500)
    Phone=models.CharField(max_length=12)
    email = models.EmailField()
    def __str__(self):
        return self.name

class recruitment_notice(models.Model):
    notice=models.CharField(max_length=1000)
    def __str__(self):
        return self.notice

class download_link(models.Model):
    title=models.CharField(max_length=1000)
    file=models.FileField(upload_to="pdf/")
    def __str__(self):
        return self.title
