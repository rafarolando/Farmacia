__author__ = 'Rafael'

from django.forms import ModelForm

from medicamentos.models import Proveedores, Unidades, Compuestos, Medicamentos

class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedores

class UnidadesForm(ModelForm):
    class Meta:
        model = Unidades

class CompuestoForm(ModelForm):
    class Meta:
        model = Compuestos

class MedicamentoForm(ModelForm):
    class Meta:
        model = Medicamentos