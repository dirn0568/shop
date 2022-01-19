# Generated by Django 3.2.8 on 2022-01-18 15:16

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
            name='Resume_Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_title_detail', models.CharField(max_length=2000)),
                ('resume_date', models.DateField(auto_now=True)),
                ('resume_Time', models.TimeField(auto_now=True)),
                ('resume_open', models.IntegerField(default=1)),
                ('resume_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_title', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_title', models.CharField(max_length=100)),
                ('resume_school', models.TextField(blank=True, max_length=1000, null=True)),
                ('resume_career', models.TextField(blank=True, max_length=1000, null=True)),
                ('resume_text', models.TextField(blank=True, max_length=10000, null=True)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_Resume_Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_certificate', models.FileField(blank=True, null=True, upload_to='resume_file/')),
                ('certificate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificate', to='resumeapp.user_resume')),
            ],
        ),
        migrations.CreateModel(
            name='Resume_UniversitySchool_Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_university_major_list', models.CharField(max_length=200)),
                ('resume_university_major_detail', models.CharField(max_length=200)),
                ('resume_university_major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_university_major', to='resumeapp.resume_title')),
            ],
        ),
        migrations.CreateModel(
            name='Resume_UniversitySchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_study_year', models.CharField(max_length=50)),
                ('university_school_name', models.CharField(max_length=50)),
                ('university_field_name', models.CharField(max_length=50)),
                ('university_start_time', models.CharField(max_length=200)),
                ('university_end_time', models.CharField(max_length=200)),
                ('university_study_time', models.CharField(max_length=200)),
                ('university_study_level', models.CharField(max_length=200)),
                ('university_finaltest', models.CharField(max_length=2000)),
                ('resume_university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_university', to='resumeapp.resume_title')),
            ],
        ),
        migrations.CreateModel(
            name='Resume_Self_Introduce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_self_introduce_title', models.CharField(max_length=500)),
                ('resume_self_introduce_text', models.CharField(max_length=3000)),
                ('resume_self_introduce', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_self_introduce', to='resumeapp.resume_title')),
            ],
        ),
        migrations.CreateModel(
            name='Resume_Prize_Play',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_prize_certificate', models.CharField(max_length=500)),
                ('resume_prize_place', models.CharField(max_length=500)),
                ('resume_prize_title', models.CharField(max_length=500)),
                ('resume_prize_date', models.CharField(max_length=500)),
                ('resume_prize_play', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_prize_play', to='resumeapp.resume_title')),
            ],
        ),
        migrations.CreateModel(
            name='Resume_Port_Polio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_port_polio_detail', models.FileField(upload_to='')),
                ('resume_port_polio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_port_polio', to='resumeapp.resume_title')),
            ],
        ),
        migrations.CreateModel(
            name='Resume_Out_Play',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_out_activity', models.CharField(max_length=500)),
                ('resume_out_place', models.CharField(max_length=500)),
                ('resume_out_start_play', models.CharField(max_length=500)),
                ('resume_out_end_play', models.CharField(max_length=500)),
                ('resume_out_play_text', models.CharField(max_length=500)),
                ('resume_out_play', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_out_play', to='resumeapp.resume_title')),
            ],
        ),
        migrations.CreateModel(
            name='Resume_MiddleSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_school_name', models.CharField(max_length=50)),
                ('middle_field_name', models.CharField(max_length=50)),
                ('middle_start_time', models.CharField(max_length=200)),
                ('middle_end_time', models.CharField(max_length=200)),
                ('resume_middle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_middle', to='resumeapp.resume_title')),
            ],
        ),
        migrations.CreateModel(
            name='Resume_Hope_Work_Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_hope_work_work1', models.CharField(max_length=200)),
                ('resume_hope_work_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_hope_work_work', to='resumeapp.resume_title')),
            ],
        ),
        migrations.CreateModel(
            name='Resume_Hope_Work_Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_hope_work_field1', models.CharField(max_length=200)),
                ('resume_hope_work_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_hope_work_field', to='resumeapp.resume_title')),
            ],
        ),
        migrations.CreateModel(
            name='Resume_Hope_Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_hope_work_start_time', models.CharField(max_length=200)),
                ('resume_hope_work_end_time', models.CharField(max_length=200)),
                ('resume_hope_work_money', models.CharField(max_length=200)),
                ('resume_hope_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_hope_work', to='resumeapp.resume_title')),
            ],
        ),
        migrations.CreateModel(
            name='Resume_HighSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('high_school_name', models.CharField(max_length=50)),
                ('high_field_name', models.CharField(max_length=50)),
                ('high_start_time', models.CharField(max_length=200)),
                ('high_end_time', models.CharField(max_length=200)),
                ('high_major', models.CharField(max_length=200)),
                ('resume_high', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_high', to='resumeapp.resume_title')),
            ],
        ),
        migrations.CreateModel(
            name='Resume_ElementarySchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elementary_school_name', models.CharField(max_length=50)),
                ('elementary_field_name', models.CharField(max_length=50)),
                ('elementary_start_time', models.CharField(max_length=200)),
                ('elementary_end_time', models.CharField(max_length=200)),
                ('resume_elementary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_elementary', to='resumeapp.resume_title')),
            ],
        ),
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
        migrations.CreateModel(
            name='Resume_Career_Ability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_career_ability_text', models.CharField(max_length=2000)),
                ('resume_career_ability', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_career_ability', to='resumeapp.resume_title')),
            ],
        ),
        migrations.CreateModel(
            name='Resume_Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume_company_name', models.CharField(max_length=50)),
                ('resume_career_start_time', models.CharField(max_length=200)),
                ('resume_career_end_time', models.CharField(max_length=200)),
                ('resume_career_out', models.CharField(max_length=200)),
                ('resume_career_position', models.CharField(max_length=200)),
                ('resume_career_position_detail', models.CharField(max_length=200)),
                ('resume_career_money', models.CharField(max_length=20000)),
                ('resume_career_money_detail', models.CharField(max_length=200)),
                ('resume_career_position_detail2', models.CharField(max_length=200)),
                ('resume_career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_career', to='resumeapp.resume_title')),
            ],
        ),
    ]
