from django.db import models

# Create your models here.

class Turnos(models.Model):
    fecha = models.DateField
    def __unicode__(self):
        return self.fecha
