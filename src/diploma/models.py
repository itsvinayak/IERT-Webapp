from django.db import models


class diploma_facultys(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(
        null=True,
        blank=True,
        default="profile_pics/default.jpg",
        upload_to="media/teachers_img/",
    )
    Designation = models.CharField(max_length=400)
    branch = models.CharField(max_length=100, null=True, blank=True)
    Qualification = models.CharField(max_length=500)
    Phone = models.CharField(max_length=12)
    email = models.EmailField()

    def __str__(self):
        return self.name
