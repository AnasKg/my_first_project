# Generated by Django 3.2.4 on 2021-06-09 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_student_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name': 'филиал', 'verbose_name_plural': 'филиалы'},
        ),
    ]
