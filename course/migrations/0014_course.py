# Generated by Django 3.2.4 on 2021-06-24 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_branch_creator'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]