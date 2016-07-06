from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=200)
    number = models.CharField(max_length=200)

    def __str__(self):
        return self.name
