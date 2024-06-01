from django.db import models


# Create your models here.


class Area(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Organization(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    opened = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Construction(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    field = models.CharField(max_length=100)
    floor = models.IntegerField(default=0)
    parkinglot = models.BooleanField(default=None)
    playground = models.BooleanField(default=None)
    elevator = models.BooleanField(default=None)

    def __str__(self):
        return self.name
