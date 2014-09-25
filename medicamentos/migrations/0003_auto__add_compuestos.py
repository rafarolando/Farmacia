# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Compuestos'
        db.create_table(u'medicamentos_compuestos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length='50')),
            ('dosis', self.gf('django.db.models.fields.IntegerField')()),
            ('unidad', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['medicamentos.Unidades'], unique=True)),
        ))
        db.send_create_signal(u'medicamentos', ['Compuestos'])


    def backwards(self, orm):
        # Deleting model 'Compuestos'
        db.delete_table(u'medicamentos_compuestos')


    models = {
        u'medicamentos.compuestos': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Compuestos'},
            'dosis': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            'unidad': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['medicamentos.Unidades']", 'unique': 'True'})
        },
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