from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(null=False, blank=False)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
