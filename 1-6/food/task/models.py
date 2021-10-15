from django.db import models
from django.db.models.base import Model

# Create your models here.
class Task(models.Model):
    makanan = models.TextField(default='', max_length= 200)
    jenismakanan = models.CharField(max_length=20)
    jumlahmakanan = models.IntegerField(default=0)
    minuman = models.TextField(default='' ,max_length= 200)
    jenisminuman = models.CharField(max_length=20)
    jumlahminuman = models.IntegerField(default=0)
    harga = models.IntegerField(default=0)

