from django.db import models

class Inventario(models.Model):
    id_inventario = models.CharField(primary_key=True, max_length=6)
    cantidad_actual = models.PositiveIntegerField()  
    cantidad_minima = models.PositiveSmallIntegerField()    
    fecha_actualizacion = models.DateField()  
    ubicacion = models.CharField(max_length=100)  
    historial = models.TextField(blank=True, null=True)  

    def __str__(self):
        return self.id_inventario
