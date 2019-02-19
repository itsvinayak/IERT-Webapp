from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class User_details(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no=models.CharField(default='', max_length=20)
    branch=models.CharField(default='', max_length=20)
    year = models.CharField(default='', max_length=20)
    roll_no=models.CharField(default='', max_length=30)
    date_of_birth=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} profile details'
