# Generated by Django 2.2 on 2019-10-12 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iert_news', '0021_auto_20190810_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='no_of_comment',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
