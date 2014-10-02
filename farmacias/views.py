from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.contrib import  messages
from django.contrib.auth.decorators import permission_required
from django.db.models import Q

from farmacia.log_admin import admin_log_addition, admin_log_change
from farmacia.reportes import generar_pdf

import datetime

from farmacias.models import Categoria, Farmacia, Turno
from farmacias.form import CategoriaForm, FarmaciaForm, TurnoForm

#CATEGORIAS
@permission_required('categorias.add_categoria', login_url="/login")
def index_categoria(request):
    categorias = Categoria.objects.all()
    return render (request, 'categorias/base_categorias.html',{
        'categorias':categorias,
    })

@permission_required('categorias.add.categoria', login_url="/login")
def nueva_categoria(request):
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            c = formulario.save()
            admin_log_addition(request, c, 'Categoria creada')
            sms = "Categoria %s Creada Correctamente"%(c.tipo)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index_categoria))
    else:
        formulario = CategoriaForm()
    return render(request, 'categorias/nueva_categoria.html',{
        'formulario':formulario,
    })

@permission_required('categorias.add_categoria', login_url="/login")
def modificar_categoria (request, pk):
    formularioMod = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST, instance=formularioMod)
        if formulario.is_valid():
            c = formulario.save()
            admin_log_change(request, c, 'Categoria Modificada')
            sms = "Categoria %s Modificada Correctamente"%(c.tipo)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index_categoria))
    else:
        formulario = CategoriaForm(instance=formularioMod)
    return render(request, 'categorias/modificar_categoria.html',{
        'formulario':formulario,
    })

#FARMACIAS
@permission_required('farmacias.add_farmacia', login_url='/login')
def index_farmacia(request):
    farmacias = Farmacia.objects.all()
    return render(request, 'farmacias/base_farmacias.html',{
        'farmacias':farmacias,
    })

@permission_required('farmacias.add_farmacia', login_url='/login')
def nueva_farmacia (request):
    if request.method == 'POST':
        formulario = FarmaciaForm(request.POST)
        if formulario.is_valid():
            c = formulario.save()
            admin_log_change(request, c, 'Farmacia Creada')
            sms = "Farmacia %s Creada Correctamente"%(c.tipo)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index_farmacia))
    else:
        formulario = FarmaciaForm()
    return render(request, 'farmacias/nueva_farmacia.html',{
        'formulario':formulario,
    })
@permission_required('farmacias.add_farmacia', login_url='/login')
def modificar_farmacia (request, pk):
    formularioMod = get_object_or_404(Farmacia, pk=pk)
    if request.method == 'POST':
        formulario = FarmaciaForm(request.POST, instance=formularioMod)
        if formulario.is_valid():
            c = formulario.save()
            admin_log_change(request, c, 'Farmacia Modificada')
            sms = "Farmacia %s Modificada Correctamente"%(c.tipo)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index_farmacia))
    else:
        formulario = FarmaciaForm(instance=formularioMod)
    return render(request, 'farmacias/modificar_farmacia.html',{
        'formulario':formulario,
    })

#TURNOS

@permission_required('turnos.add_turno', login_url='/login')
def index_turno (request):
    turnos = Turno.objects.all()
    return  render(request, 'turnos/base_turno.html',{
        'turnos':turnos,
    })

@permission_required('turnos.add_turno', login_url='/login')
def nuevo_turno (request):
    if request.method == 'POST':
        formulario = TurnoForm(request.POST)
        if formulario.is_valid():
            c = formulario.save()
            admin_log_addition(request,c ,'Turno Creado')
            sms = "Turno %s Creado Correctamente"%(c.tipo)
            messages.success(request, sms)
            return  HttpResponseRedirect(reverse(index_turno))
    else:
        formulario = TurnoForm()
    return render(request, 'turnos/nuevo_turno.html',{
        'formulario':formulario,
    })

@permission_required('turnos.add_turno', login_url='/login')
def modificar_turno (request, pk):
    formularioMod = get_object_or_404(Turno, pk=pk )
    if request.method == 'POST':
        formulario = TurnoForm(request.POST, instance = formularioMod)
        if formulario.is_valid():
            c = formulario.save()
            admin_log_change(request, c, 'Turno Modificado')
            sms = "Turno %s Modificado Correctamente"%(c.tipo)
            messages.success(request, sms)
            return HttpResponseRedirect(reverse(index_turno))
    else:
        formulario = TurnoForm(instance=formularioMod)
    return render(request, 'turnos/modificar_turno.html',{
        'formulario':formulario,
    })



def Buscar (request):
    query = request.get('q')
    tipo = Categoria.objects.filter(tipo__icontains = query)
    return render(request, "categorias/buscar.html",{
        'query':query,
    })