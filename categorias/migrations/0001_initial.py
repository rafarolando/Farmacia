# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categoria'
        db.create_table(u'categorias_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(max_length='50')),
        ))
        db.send_create_signal(u'categorias', ['Categoria'])


    def backwards(self, orm):
        # Deleting model 'Categoria'
        db.delete_table(u'categorias_categoria')


    models = {
        u'categorias.categoria': {
            'Meta': {'ordering': "['tipo']", 'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': "'50'"})
        }
    }

    complete_apps = ['categorias']