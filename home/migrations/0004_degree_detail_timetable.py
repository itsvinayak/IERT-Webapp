# Generated by Django 2.1.5 on 2019-02-27 10:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_gallery_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='degree_detail',
            name='timetable',
            field=models.TextField(default=datetime.datetime(2019, 2, 27, 10, 2, 49, 237356, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
