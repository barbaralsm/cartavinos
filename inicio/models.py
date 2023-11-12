from django.db import models

# Create your models here.
class vinos(models.Model):
    marca=models.CharField (max_length=30)  
    bodega=models.CharField(max_length=30)
    cepa=models.CharField(max_length=30)
    cosecha=models.IntegerField()
    precio= models.IntegerField()
    
class regiones(models.Model):
    nombre=models.CharField (max_length=30)  
    provincias=models.CharField(max_length=30)
    clima=models.CharField(max_length=30)
    suelo=models.IntegerField()
    cepas= models.IntegerField()
    bodegas=models.TextField()
    
class maridajes(models.Model):
    cepa=models.CharField (max_length=30)  
    maridaje=models.CharField(max_length=30)
    marcasrecomendadas=models.TextField()
    
class tips(models.Model):  
    etiqueta=models.TextField()  
    maridaje=models.CharField(max_length=30)
    reseñas=models.TextField()
