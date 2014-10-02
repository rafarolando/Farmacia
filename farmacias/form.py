__author__ = 'Rafael'

from django.forms   import ModelForm
from farmacias.models import Farmacia, Categoria, Turno


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria

class FarmaciaForm(ModelForm):
    class Meta:
        model = Farmacia


class TurnoForm (ModelForm):
    class Meta:
        model = Turno