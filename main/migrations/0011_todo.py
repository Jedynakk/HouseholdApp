# Generated by Django 4.1.5 on 2023-05-21 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_household_expense_household_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=64)),
                ('done', models.BooleanField(default=False)),
                ('until', models.DateField(null=True)),
                ('household', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.household')),
            ],
        ),
    ]
