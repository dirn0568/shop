# Generated by Django 3.2.2 on 2022-01-06 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume_title',
            name='resume_Time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='resume_title',
            name='resume_date',
            field=models.DateField(auto_now=True),
        ),
    ]