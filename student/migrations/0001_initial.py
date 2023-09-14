# Generated by Django 4.2.4 on 2023-09-14 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_of_student', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('gender', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('date_of_joined', models.DateField()),
                ('photo', models.ImageField(null=True, upload_to='uploads/')),
                ('created_at', models.DateField(auto_now=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.parent')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('remark', models.IntegerField()),
                ('created_at', models.DateField(auto_now=True)),
                ('student', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
