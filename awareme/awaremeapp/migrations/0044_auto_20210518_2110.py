# Generated by Django 3.1.7 on 2021-05-18 15:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('awaremeapp', '0043_auto_20210518_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='ngo',
        ),
        migrations.AddField(
            model_name='donation',
            name='ngo',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
