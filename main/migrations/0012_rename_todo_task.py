# Generated by Django 4.1.5 on 2023-05-21 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_todo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ToDo',
            new_name='Task',
        ),
    ]