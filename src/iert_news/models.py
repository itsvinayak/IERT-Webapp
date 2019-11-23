from django.db import models
from django.contrib.auth.models import User


class new(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    date = models.DateField(null=True, blank=True)
    no_of_comment = models.IntegerField(blank=True, default=0)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="media/")
    info = models.TextField()

    def __str__(self):
        return self.title


class new_by_viewer(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=300)
    date = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="media/")
    info = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    news = models.ForeignKey(new, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # in place of self we can also use Comment here
    reply = models.ForeignKey(
        "self", null=True, related_name="replies", on_delete=models.CASCADE
    )
    content = models.CharField(max_length=300)
    time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return "{} --> {}".format(str(self.user.username), self.news.title)
