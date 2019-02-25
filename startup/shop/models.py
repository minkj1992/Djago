from django.db import models

# Create your models here.
class Product(models.Model):
    idx = models.CharField(null=True,max_length=20)
    # title = models.CharField(null=True,max_length=20)
    # price = models.CharField(null=True,max_length=20)
    # like = models.CharField(null=True,max_length=20)
    pic = models.ImageField(null=True,upload_to='search')