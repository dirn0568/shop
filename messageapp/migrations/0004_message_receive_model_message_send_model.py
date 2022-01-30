# Generated by Django 3.2.8 on 2022-01-30 09:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messageapp', '0003_message_resume_model_message_date_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message_Send_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_send_detail', models.CharField(max_length=2000)),
                ('message_send_date', models.DateField(auto_now=True)),
                ('message_send_Time', models.TimeField(auto_now=True)),
                ('message_send_date_time', models.DateTimeField(auto_now=True)),
                ('message_send_receive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_send_receive', to=settings.AUTH_USER_MODEL)),
                ('message_send_send', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_send_send', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message_Receive_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_receive_detail', models.CharField(max_length=2000)),
                ('message_receive_date', models.DateField(auto_now=True)),
                ('message_receive_Time', models.TimeField(auto_now=True)),
                ('message_receive_date_time', models.DateTimeField(auto_now=True)),
                ('message_receive_receive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_receive_receive', to=settings.AUTH_USER_MODEL)),
                ('message_receive_send', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_receive_send', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
