#encoding:utf-8
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

from categorias.models import Categoria
from categorias.form import CategoriaForm

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