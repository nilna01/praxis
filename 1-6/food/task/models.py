from django.db import models
from django.db.models.base import Model

# Create your models here.
class Task(models.Model):
    makanan = models.TextField(max_length= 200)
    harga = models.IntegerField()
    jumlah = models.IntegerField()
