# Generated by Django 2.1.5 on 2019-03-31 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20190331_0639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='degree_detail',
            name='image',
        ),
    ]
