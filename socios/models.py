from django.db import models


class Plan(models.Model):
    nombre = models.CharField(max_length=100)
    precio_mensual = models.DecimalField(max_digits=8, decimal_places=0)

    def __str__(self):
        return self.nombre


class Socio(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT, related_name='socios')
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    fecha_inscripcion = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
