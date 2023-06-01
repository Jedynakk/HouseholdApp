from django.db import models
from accounts.models import User

UNIT = (
    (1, 'kg'),
    (2, 'l'),
    (3, 'pieces')
)


class Household(models.Model):
    name = models.CharField(max_length=16, blank=False,
                            null=False, unique=True)
    password = models.CharField(max_length=16, blank=False, null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


class Housemate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    houseHold = models.ForeignKey(
        Household, on_delete=models.CASCADE, null=False)


class Product(models.Model):
    household = models.ForeignKey(
        Household, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=16, blank=False, null=False)
    quantity = models.PositiveIntegerField(default=0)
    unit = models.IntegerField(choices=UNIT, default=1)


class Expense(models.Model):
    household = models.ForeignKey(
        Household, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=16, blank=False, null=False)
    charge = models.IntegerField(default=0)
    isPayed = models.BooleanField(default=False)
    until = models.DateField()


class Task(models.Model):
    household = models.ForeignKey(
        Household, on_delete=models.CASCADE, null=False)
    text = models.CharField(max_length=16, blank=False, null=False)
    done = models.BooleanField(default=False)
    until = models.DateField(null=True)
