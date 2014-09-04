from django.shortcuts import render, render_to_response
from django.template import RequestContext
# Create your views here.
def medicamentos (request):
    return render_to_response('farmacias/base_farmacias.html', {

    },context_instance=RequestContext(request))

def formulario (request):
    return render_to_response('farmacias/form_medicamentos.html', {

    },context_instance=RequestContext(request))

def formulario_turno (request):
    return render_to_response('farmacias/form_turno.html', {

    },context_instance=RequestContext(request))