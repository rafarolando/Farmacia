from django.db import models

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
