from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.contrib import  messages
from django.contrib.auth.decorators import permission_required

from farmacia.log_admin import admin_log_addition, admin_log_change
from farmacia.reportes import generar_pdf

import datetime

from medicamentos.models import Proveedores, Unidades, Compuestos
from medicamentos.form import ProveedorForm, UnidadesForm, CompuestoForm

#PROVEEDORES
@permission_required('proveedores.add_proveedor', login_url='/login')
def index_proveedor (request):
    proveedores = Proveedores.objects.all()

    return render(request, 'proveedores/base_proveedores.html',{
        'proveedores':proveedores,
    })

@permission_required('proveedores.add_proveedor', login_url='/login')
def nuevo_proveedor(request):
    if request.method == 'POST':
        formulario = ProveedorForm(request.POST)
        if formulario.is_valid():
            c = formulario.save()
            admin_log_addition(request, c, 'Proveedor creado')
            sms = "Proveedor %s Creado Correctamene"%(c.proveedor)
            messages.success(request, sms)
            return  HttpResponseRedirect(reverse(index_proveedor))
    else:
        formulario = ProveedorForm()
    return render(request, 'proveedores/nuevo_proveedor.html',{
        'formulario':formulario,
    })

#UNIDADES
@permission_required('unidades.add_unidad', login_url='/login')
def index_unidad (request):
    unidades = Unidades.objects.all()
    return render(request, 'unidades/base_unidad.html',{
        'unidades':unidades,
    })

@permission_required('unidades.add_unidad', login_url='/login')
def nueva_unidad (request):
    if request.method == 'POST':
        formulario = UnidadesForm(request.POST)
        if formulario.is_valid():
            c = formulario.save()
            admin_log_addition(request, c, 'Unidad creada')
            sms = "Unidad %s Creada Correctamente"%(c.unidad)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index_unidad))
    else:
        formulario = UnidadesForm()
    return render(request, 'unidades/nueva_unidad.html',{
        'formulario':formulario,
    })

#COMPUESTOS
@permission_required('compuestos.add_compuesto', login_url='/login')
def index_compuesto (request):
    compuestos = Compuestos.objects.all()
    return render(request, 'compuestos/base_compuesto.html',{
        'compuestos':compuestos,
    })

@permission_required('compuestos.add_compuesto', login_url='/login')
def nuevo_compuesto (request):
    if request.method == 'POST':
        formulario = CompuestoForm(request.POST)
        if formulario.is_valid ():
            c= formulario.save()
            admin_log_addition(request, c,'Compuesto creado')
            sms = "Compuesto %s Creado Correctamente"%(c.compuesto)
            messages.success(request,sms)
            return HttpResponseRedirect(reverse(index_compuesto))
    else:
        formulario = CompuestoForm()
    return render(request, 'compuestos/nuevo_compuesto.html',{
        'formulario':formulario,
    })