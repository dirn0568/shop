# Generated by Django 3.2.8 on 2022-03-26 03:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Test_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Message_Send_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_send_title', models.CharField(max_length=2000)),
                ('message_send_detail', models.TextField()),
                ('message_send_date', models.DateField(auto_now=True)),
                ('message_send_Time', models.TimeField(auto_now=True)),
                ('message_send_date_time', models.DateTimeField(auto_now=True)),
                ('message_send_file', models.FileField(blank=True, null=True, upload_to='message/')),
                ('message_send_receive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_send_receive', to=settings.AUTH_USER_MODEL)),
                ('message_send_send', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_send_send', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message_Resume_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_title', models.CharField(max_length=2000)),
                ('message_detail', models.CharField(max_length=2000)),
                ('message_date', models.DateField(auto_now=True)),
                ('message_Time', models.TimeField(auto_now=True)),
                ('message_date_time', models.DateTimeField(auto_now=True)),
                ('message_file', models.FileField(blank=True, null=True, upload_to='message/')),
                ('message_resume_receive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_resume_receive', to=settings.AUTH_USER_MODEL)),
                ('message_resume_send', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_resume_send', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
