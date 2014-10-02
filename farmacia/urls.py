from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')),
    # Examples:
    # url(r'^$', 'farmacia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #url(r'^rafael/$', 'usuarios.views.home'),
    url(r'^$', 'usuarios.views.base'),

    #USUARIOS
    url(r'^usuario/new/$', 'usuarios.views.new_user'),
    url(r'^login/$', 'usuarios.views.logget_in'),
    url(r'^usuario/perfil/$', 'usuarios.views.perfil'),
    url(r'^logout/$', 'usuarios.views.salir'),

    #FARMACIA
    #url(r'^medicamentos/&', 'farmacias.views.medicamentos'),
    #url(r'^form/&','farmacias.views.formulario'),

    #FARMACIAS
    url(r'^tipos/$','farmacias.views.index_categoria'),
    url(r'^tipos/nuevo/$','farmacias.views.nueva_categoria'),
    url(r'^tipo/modificar/(?P<pk>\d+)$', 'farmacias.views.modificar_categoria'),
    url(r'^farmacia/$','farmacias.views.index_farmacia'),
    url(r'^farmacia/nuevo/$','farmacias.views.nueva_farmacia'),
    url(r'^farmacia/modificar/(?P<pk>\d+)$', 'farmacias.views.modificar_farmacia'),
    url(r'^turno/$','farmacias.views.index_turno'),
    url(r'^turno/nuevo/$','farmacias.views.nuevo_turno'),
    url(r'^turno/modificar/(?P<pk>\d+)$', 'farmacias.views.modificar_turno'),
    url(r'^buscar/$', 'farmacias.views.Buscar'),

    #MEDICAMENTOS
    url(r'^proveedores/$','medicamentos.views.index_proveedor'),
    url(r'^proveedores/nuevo/$','medicamentos.views.nuevo_proveedor'),
    url(r'^proveedores/modificar/(?P<pk>\d+)$', 'medicamentos.views.modificar_proveedor'),
    url(r'^unidad/$','medicamentos.views.index_unidad'),
    url(r'^unidades/nuevo/$','medicamentos.views.nueva_unidad'),
    url(r'^unidades/modificar/(?P<pk>\d+)$', 'medicamentos.views.modificar_unidad'),
    url(r'^compuestos/$','medicamentos.views.index_compuesto'),
    url(r'^compuestos/nuevo/$','medicamentos.views.nuevo_compuesto'),
    url(r'^compuestos/modificar/(?P<pk>\d+)$', 'medicamentos.views.modificar_compuesto'),
    url(r'^medicamentos/$','medicamentos.views.index_medicamento'),
    url(r'^medicamentos/nuevo/$','medicamentos.views.nuevo_medicamento'),
    url(r'^medicamnetos/modificar/(?P<pk>\d+)$', 'medicamentos.views.modificar_medicamento'),
)
