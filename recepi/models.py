from django.db import models

# Create your models here.
class Receipe(models.Model):
    name = models.CharField(max_length=255)
    descp = models.TextField()
    img=models.ImageField(upload_to="receipe")