# Generated by Django 4.1.5 on 2023-05-21 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]
