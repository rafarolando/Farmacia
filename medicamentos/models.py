#encoding:utf-8
from django.db import models

# Create your models here.

class Proveedores (models.Model):
    nombre = models.CharField(max_length='50',verbose_name='Nombre de Industria')
    encargado = models.CharField(max_length='50')
    telefono = models.CharField(max_length='20', verbose_name='Teléfono - Celular')
    direccion = models.CharField(max_length='20')
    correo = models.EmailField(verbose_name='Correo Electronico')

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = 'Nombres'
        permissions = (
            ('detail_proveedores', 'Detalle de Industria'),
            ('report_proveedores', 'Reporte de Industria'),
        )


class Unidades (models.Model):
    nombre = models.CharField(max_length='50')
    sigla = models.CharField(max_length='5')
    descripcion = models.CharField(max_length='50')

    def __unicode__(self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = 'Nombres'
        permissions = (
            ('detail_unidades', 'Detalle de Unidad de Medida'),
            ('report_unidades', 'Reporte de Unidad de Medida'),
        )


class Compuestos (models.Model):
    nombre = models.CharField(max_length='50')
    dosis = models.IntegerField()
    unidad = models.OneToOneField(Unidades)

    def __unicode__(self):
        return  self.nombre
    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = 'Nombres'
        permissions = (
            ('detail_compuestos', 'Detalle de Compuesto'),
            ('report_compuestos', 'Reporte de Compuesto'),
        )


class Medicamentos (models.Model):
    nombre = models.CharField(max_length='50', verbose_name='Nombre del Medicamento')
    proveedor = models.OneToOneField(Proveedores)
    compuesto = models.ForeignKey(Compuestos)

    def __unicode__(self):
        return  self.nombre

    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = 'Nombres'
        permissions = (
            ('detail_medicamentos', 'Detalle del Medicamento'),
            ('report_medicamentos', 'Reporte del Medicamento'),
        )