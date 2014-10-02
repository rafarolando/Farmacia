#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from medicamentos.models import Medicamentos

class Categoria (models.Model):
    tipo = models.CharField(max_length='50')

    def __unicode__(self):
        return self.tipo
    class Meta:
        ordering = ['tipo']
        verbose_name_plural = 'Tipos'
        permissions = (
            ('detail_categoria', 'Detalle de Tipo'),
            ('report_categoria', 'Reporte de Tipo'),
        )


class Farmacia(models.Model):
    nombre = models.CharField(max_length='100', verbose_name='Nombre de Farmacia')
    direccion = models.CharField(max_length='200')
    telefono = models.CharField(max_length='50', verbose_name='Telefono - Celular')
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='imgfarmacia')
    #ciudades =(
    #    ('Potosi','Potosi'),
    #    ('Sucre', 'Sucre'),
    #    ('Oruro', 'Oruro'),
    #    )
    #ciudad = models.CharField(max_length='20', default='Potosi', choices=ciudades)
    latitud = models.CharField(max_length='50', null=True, blank=True)
    longitud = models.CharField(max_length='50', null=True, blank=True)
    usuario = models.ForeignKey(User, null=True, blank=True)
    categoria = models.OneToOneField (Categoria)
    medicamentos = models.ManyToManyField (Medicamentos)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ['-nombre']
        verbose_name_plural = 'Farmacias Registradas'
        permissions = (
            ('detail_farmacias', 'Detalle de la Farmacia'),
            ('report_farmacias', 'Reporte de la Farmacia'),
        )
    #OneToOneField() ManyToManyField()
    #text integer float decimal char date time datetime email url

#class Pais(models.Model):
#    nombre = models.CharField(max_length='50')
#    farmacia = models.OneToOneField(Farmacia)
#    def __unicode__(self):
#        return self.farmacia.nombre
#    class Meta:
#        ordering = ['-nombre']
#        verbose_name_plural = 'Paises'


class Turno (models.Model):
    fecha = models.DateField()
    farmacia = models.ForeignKey(Farmacia)
    def __unicode__(self):
        return  self.fecha
    class Meta:
        ordering = ['fecha']
        verbose_name_plural = "Turnos a Cumplir"
        permissions = (
            ('detail_turnos', 'Detalle de Turno'),
            ('report_turnos', 'Reporte de Truno'),
        )