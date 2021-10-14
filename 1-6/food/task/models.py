from django.db import models
from django.db.models.base import Model

# Create your models here.
class Task(models.Model):
    makanan = models.TextField(default='', max_length= 200)
    minuman = models.TextField(default='' ,max_length= 200)
    harga = models.IntegerField(default='')
    jumlah = models.IntegerField(default='')

