# Generated by Django 3.1.7 on 2021-05-06 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210506_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
