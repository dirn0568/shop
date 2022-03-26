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
            name='User_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_birthday', models.CharField(max_length=100)),
                ('user_gender', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=100)),
                ('user_page', models.CharField(max_length=100)),
                ('profile_text', models.TextField(blank=True, max_length=1000, null=True)),
                ('profile_img', models.ImageField(blank=True, null=True, upload_to='Profile_img/')),
                ('user_open', models.IntegerField(default=1)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
