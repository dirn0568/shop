# Generated by Django 3.2.8 on 2022-02-15 14:04

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
            name='FriendRequestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='A_User', to=settings.AUTH_USER_MODEL)),
                ('B_User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='B_User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
