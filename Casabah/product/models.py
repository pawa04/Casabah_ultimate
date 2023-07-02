from django.db import models

# Create your models here.


class Pastry(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField("Ingredients")
    description = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # How to return different values
        data = "{description},{name}"
        return self.name

class Ingredients(models.Model) :

    name= models.CharField(max_length=50,unique=True)
    def __str__(self):
        # How to return different values
        return self.name
