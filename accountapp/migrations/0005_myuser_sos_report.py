# Generated by Django 3.2.8 on 2022-06-02 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0004_myuser_company_paper'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='sos_report',
            field=models.IntegerField(default=0),
        ),
    ]