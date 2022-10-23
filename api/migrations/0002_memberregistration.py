# Generated by Django 4.0 on 2022-10-01 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('email', models.EmailField(default=None, max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('I prefer not to say', 'I prefer not to say')], default='Male', max_length=100)),
                ('roll_no', models.CharField(default=None, max_length=10)),
                ('degree', models.CharField(choices=[('B.Tech', 'B.Tech'), ('B.Tech + M.Tech (Dual Degree)', 'B.Tech + M.Tech (Dual Degree)')], default='B.Tech', max_length=60)),
                ('branch', models.CharField(choices=[('Computer Science and Engineering', 'Computer Science and Engineering'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Electrical Engineering', 'Electrical Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Material Science and Engineering', 'Material Science and Engineering'), ('Mathematics and Computing', 'Mathematics and Computing'), ('Engineering Physics', 'Engineering Physics'), ('Other', 'Other')], max_length=60)),
                ('year', models.PositiveIntegerField(blank=True, null=True)),
                ('phone', models.CharField(default=None, max_length=10)),
                ('home_state', models.CharField(default=None, max_length=50)),
                ('skills', models.TextField()),
                ('strength', models.TextField()),
                ('weakness', models.TextField()),
                ('achievement', models.TextField()),
                ('application_response', models.TextField()),
                ('supporting_docs_link', models.URLField(blank=True, null=True)),
                ('photograph_link', models.URLField(blank=True, null=True)),
                ('sign_link', models.URLField(blank=True, null=True)),
                ('acknowledgement', models.BooleanField(default=False)),
            ],
        ),
    ]
