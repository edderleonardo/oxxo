from django.db import models


class Colony(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Oxxo(models.Model):
    name = models.CharField(max_length=50)
    colony = models.ForeignKey(
        Colony, on_delete=models.CASCADE)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    allday = models.BooleanField(default=False)
    beer = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)

    def __str__(self):
        return self.name
