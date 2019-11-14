from django.db import models


class notice_board(models.Model):
    topic = models.CharField(max_length=300)
    branch = models.CharField(
        max_length=100,
        choices=[
            ("all", "all"),
            ("Computer Science & Engineering", "Computer Science & Engineering"),
            ("Electronic Engineering", "Electronic Engineering"),
            (
                "Industrial & Production Engineering",
                "Industrial & Production Engineering",
            ),
            ("Electrical Engineering", "Electrical Engineering"),
            ("Civil Engineering", "Civil Engineering"),
            ("Mechanical Engineering", "Mechanical Engineering"),
            (
                "Instrumentation and Control Engineering",
                "Instrumentation and Control Engineering",
            ),
            ("Applied Science and Humanity", "Applied Science and Humanity"),
            ("Management", "Management"),
        ],
    )
    date = models.DateTimeField()
    info = models.TextField()

    def __str__(self):
        return self.topic
