# Generated by Django 3.1.7 on 2021-05-03 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awaremeapp', '0030_auto_20210503_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgdetail',
            name='profile_pic',
            field=models.ImageField(blank=True, default='\\static\\images\\default.png', null=True, upload_to=''),
        ),
    ]
