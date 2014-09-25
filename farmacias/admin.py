from django.contrib import admin
from farmacias.models import Farmacia

 #Register your models here.
class farmaciaopcion (admin.ModelAdmin):
    list_display = ['nombre','direccion','telefono']


admin.site.register(Farmacia,farmaciaopcion)
