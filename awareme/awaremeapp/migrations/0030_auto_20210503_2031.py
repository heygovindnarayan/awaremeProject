# Generated by Django 3.1.7 on 2021-05-03 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awaremeapp', '0029_auto_20210503_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgdetail',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/static/images/default.png', null=True, upload_to=''),
        ),
    ]
