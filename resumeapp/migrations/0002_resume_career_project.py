# Generated by Django 3.2.8 on 2021-12-02 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume_Career_Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_career_project_text', models.CharField(max_length=2000)),
                ('resume_career_project_start_time', models.CharField(max_length=200)),
                ('resume_career_project_end_time', models.CharField(max_length=200)),
                ('resume_career_project_text_detail', models.CharField(max_length=2000)),
                ('resume_career_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_career_project', to='resumeapp.resume_title')),
            ],
        ),
    ]
