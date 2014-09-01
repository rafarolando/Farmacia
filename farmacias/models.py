#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

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
    tipos =(
        ('Tipo 1','Tipo 1'),
        ('Tipo 2','Tipo 2'),
        ('Tipo 3','Tipo 3'),
    )
    tipo = models.CharField(max_length='10', default='Tipo 1', choices=tipos)
    latitud = models.CharField(max_length='50', null=True, blank=True)
    longitud = models.CharField(max_length='50', null=True, blank=True)
    usuario = models.ForeignKey(User, null=True, blank=True)
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ['-nombre']
        verbose_name_plural = 'Farmacias Registradas'
    #OneToOneField() ManyToManyField()
    #text integer float decimal char date time datetime email url

class Pais(models.Model):
    nombre = models.CharField(max_length='50')
    farmacia = models.OneToOneField(Farmacia)
    def __unicode__(self):
        return self.farmacia.nombre
    class Meta:
        ordering = ['-nombre']
        verbose_name_plural = 'Paises'

class Medicamentos(models.Model):
    nombre = models.CharField(max_length='100', verbose_name='Nombre del Medicamento')
    industria = models.CharField(max_length='50')
    stock = models.IntegerField()
    estado = models.BooleanField()
    farmacia = models.ManyToManyField(Farmacia)
    def __unicode__(self):
        return self.nombre
    class Meta:
        ordering = ['-nombre']
        verbose_name_plural = 'Medicamentos'

class Turno(models.Model):
    fecha = models.DateField()
    farmacia = models.ForeignKey(Farmacia, null=True, blank=True)
    def __unicode__(self):
        return self.farmacia.nombre
    class Meta:
        ordering = ['-fecha']
        verbose_name_plural = 'Turnos'

class Compuesto(models.Model):
    nombre = models.CharField(max_length='100', verbose_name='Compuesto principal')
    cantidad = models.CharField(max_length='100', verbose_name='Dosis')
    tipo = models.CharField(max_length='100')
    medicamento = models.OneToOneField(Medicamentos)
    def __unicode__(self):
        return self.nombre
    class Meta:
        ordering = ['-nombre']
        verbose_name_plural = 'Compuesto Principal'
