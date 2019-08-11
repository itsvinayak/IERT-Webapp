from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        width, height = img.size
        if height >= 300 or width >= 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class User_details(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no=models.CharField(default='',max_length=20, blank = True, null = True)
    branch=models.CharField(default='', max_length=500, blank = True, null = True)
    year = models.CharField(default='', max_length=20 ,blank = True, null = True)
    roll_no=models.CharField(default='', max_length=20 ,blank = True, null = True)
    date_of_birth=models.DateField(blank=True,null=True)

    def __str__(self):
        return f'{self.user.username} profile details'
