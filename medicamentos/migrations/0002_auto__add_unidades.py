# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Unidades'
        db.create_table(u'medicamentos_unidades', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length='50')),
            ('sigla', self.gf('django.db.models.fields.CharField')(max_length='5')),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length='50')),
        ))
        db.send_create_signal(u'medicamentos', ['Unidades'])


    def backwards(self, orm):
        # Deleting model 'Unidades'
        db.delete_table(u'medicamentos_unidades')


    models = {
        u'medicamentos.proveedores': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Proveedores'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': "'20'"}),
            'encargado': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': "'20'"})
        },
        u'medicamentos.unidades': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Unidades'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            'sigla': ('django.db.models.fields.CharField', [], {'max_length': "'5'"})
        }
    }

    complete_apps = ['medicamentos']