from django.db import models

# Create your models here.

class Rutas(models.Model):
    name = models.CharField(max_length=400, default='None')
    esp_resume = models.CharField(max_length=2000, default='None')
    eng_resume = models.CharField(max_length=2000, default='None')
    val_resume = models.CharField(max_length=2000, default='None')
    duration = models.FloatField(max_length=200, default='None')
    dificulty = models.CharField(max_length=200, default='None')
    start = models.CharField(max_length=200, default='None')
    end_point = models.CharField(max_length=200, default='None')
    image = models.CharField(max_length=200, default='None')
    url = models.CharField(max_length=200, default='None')
    transport = models.CharField(max_length=200, default='None')
    type = models.CharField(max_length=200, default='None')
    esp_description = models.CharField(max_length=4500, default='None')
    val_description = models.CharField(max_length=4500, default='None')
    eng_description = models.CharField(max_length=4500, default='None')

class Poi(models.Model):
    route = models.ForeignKey(Rutas, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, default='None')
    lat = models.FloatField()
    lon = models.FloatField()
    val_description = models.CharField(max_length=4500, default='None')
    cast_description = models.CharField(max_length=4500, default='None')
    eng_description = models.CharField(max_length=7000,  default='None')
    images = models.CharField(max_length=2500, default='None')

class Users(models.Model):
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=20, default='None')
    time = models.PositiveIntegerField()
    type = models.CharField(max_length=20, default='None')
    price = models.CharField(max_length=20, default='None')
    difficulty = models.CharField(max_length=20, default='None')
    companions = models.CharField(max_length=20, default='None')
    transport = models.CharField(max_length=20, default='None')
    time_stamp = models.DateTimeField()
    
