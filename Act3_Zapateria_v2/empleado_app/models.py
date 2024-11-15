from django.db import models

class Empleado(models.Model):
    id_empleado = models.CharField(primary_key=True, max_length=6)  
    nombre = models.CharField(max_length=100)  
    apellido = models.CharField(max_length=100)  
    horario = models.DateField()  
    salario = models.DecimalField(max_digits=10, decimal_places=2)  
    telefono = models.CharField(max_length=15, blank=True, null=True)  

    def __str__(self):
        return self.id_empleado
