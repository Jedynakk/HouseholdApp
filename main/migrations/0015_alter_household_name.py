# Generated by Django 4.1.5 on 2023-05-21 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='name',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
