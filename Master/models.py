from django.db import models
from PIL import Image
from django.core.validators import MaxValueValidator, MinValueValidator

class Mobiles(models.Model):
    brand = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    jan = models.CharField(max_length=13)
    image = models.ImageField(null= True, blank = True)
    
    
    

    def __str__(self):
        return self.model
