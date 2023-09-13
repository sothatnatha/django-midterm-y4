# Generated by Django 4.2.4 on 2023-09-13 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=20)),
                ('grade', models.ManyToManyField(default=1, to='classroom.grade')),
            ],
        ),
    ]