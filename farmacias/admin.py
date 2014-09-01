from django.contrib import admin
from farmacias.models import Farmacia,Pais,Medicamentos,Turno,Compuesto

 #Register your models here.
class farmaciaopcion (admin.ModelAdmin):
    list_display = ['nombre','direccion','telefono']


admin.site.register(Farmacia,farmaciaopcion)
admin.site.register(Pais)
admin.site.register(Medicamentos)
admin.site.register(Turno)
admin.site.register(Compuesto)