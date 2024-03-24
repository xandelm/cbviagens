from django.db import models


class Transport(models.Model):
    name = models.CharField(max_length=100)
    price_confort = models.DecimalField(max_digits=5, decimal_places=2)
    price_econ = models.DecimalField(max_digits=5, decimal_places=2)
    city = models.CharField(max_length=100)
    duration = models.DurationField()
    seat = models.CharField(max_length = 4)
    bed = models.CharField(max_length = 4)


def __str__(self):
    return self.name
