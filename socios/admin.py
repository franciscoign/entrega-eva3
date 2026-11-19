from django.contrib import admin
from .models import Plan, Socio


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio_mensual')


@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'edad', 'plan', 'fecha_inscripcion', 'activo')
    list_filter = ('plan', 'activo')
