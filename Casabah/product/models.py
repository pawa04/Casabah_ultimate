from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Pastry(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField("Ingredients")
    description = models.CharField(max_length=200, null=True)
    featured_image= models.ImageField(null= True,blank=True,default="default.jpeg",upload_to="images/")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # How to return different values
        data = "{description},{name}"
        return self.name

class Ingredients(models.Model) :

    name= models.CharField(max_length=50)
    def __str__(self):
        # How to return different values
        return self.name
