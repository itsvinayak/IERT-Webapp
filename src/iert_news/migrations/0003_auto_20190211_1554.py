# Generated by Django 2.1.5 on 2019-02-11 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("iert_news", "0002_news_image")]

    operations = [
        migrations.AlterField(
            model_name="news", name="image", field=models.ImageField(upload_to="media/")
        )
    ]