from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')),
    # Examples:
    # url(r'^$', 'farmacia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^rafael/$', 'usuarios.views.home'),
    url(r'^$', 'usuarios.views.base'),

    #USUARIOS
    url(r'^usuario/new/$', 'usuarios.views.new_user'),
    url(r'^login/$', 'usuarios.views.logget_in'),
    url(r'^usuario/perfil/$', 'usuarios.views.perfil'),
    url(r'^logout/$', 'usuarios.views.salir'),
)
