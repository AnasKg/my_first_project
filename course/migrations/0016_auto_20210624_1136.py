# Generated by Django 3.2.4 on 2021-06-24 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_student_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
