# Generated by Django 3.2.8 on 2022-01-31 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message_receive_model',
            name='message_receive_file',
            field=models.FileField(blank=True, null=True, upload_to='message/'),
        ),
        migrations.AlterField(
            model_name='message_resume_model',
            name='message_file',
            field=models.FileField(blank=True, null=True, upload_to='message/'),
        ),
        migrations.AlterField(
            model_name='message_send_model',
            name='message_send_file',
            field=models.FileField(blank=True, null=True, upload_to='message/'),
        ),
    ]
