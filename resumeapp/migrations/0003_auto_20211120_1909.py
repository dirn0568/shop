# Generated by Django 3.2.8 on 2021-11-20 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0002_auto_20211119_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume_elementaryschool',
            name='elementary_end_time',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='resume_elementaryschool',
            name='elementary_start_time',
            field=models.CharField(max_length=200),
        ),
    ]
