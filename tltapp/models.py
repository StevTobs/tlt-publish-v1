from django.db import models

# Create your models here.

class Datacustomer (models.Model):
    picplace = models.ImageField(upload_to='images',blank=True)
