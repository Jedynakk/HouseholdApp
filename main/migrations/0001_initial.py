# Generated by Django 4.1.5 on 2023-05-17 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('charge', models.PositiveIntegerField(default=0)),
                ('payed', models.BooleanField(default=False)),
                ('until', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='HouseHold',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=16)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('housemates', models.ManyToManyField(related_name='housemates', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('unit', models.IntegerField(choices=[(1, 'kg'), (2, 'l'), (3, 'pieces')], default=1)),
                ('houseHold', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.household')),
            ],
        ),
    ]
