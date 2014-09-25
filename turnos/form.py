__author__ = 'Rafael'

from django.forms import ModelForm

from turnos.models import Turnos

class TurnoForm():
    class Meta:
        model  = Turnos