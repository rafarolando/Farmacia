__author__ = 'Rafael'
from django.forms import ModelForm

from categorias.models import Categoria

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
