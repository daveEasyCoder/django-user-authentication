from django.db import models

# Create your models here.

class Products(models.Model):
    image = models.ImageField(upload_to='product_img')
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2,default=0.00)

  

