# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Farmacia.tipo'
        db.alter_column(u'farmacias_farmacia', 'tipo', self.gf('django.db.models.fields.CharField')(max_length='10'))

    def backwards(self, orm):

        # Changing field 'Farmacia.tipo'
        db.alter_column(u'farmacias_farmacia', 'tipo', self.gf('django.db.models.fields.CharField')(max_length='10', null=True))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'farmacias.compuesto': {
            'Meta': {'object_name': 'Compuesto'},
            'cantidad': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medicamento': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['farmacias.Medicamentos']", 'unique': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'tipo': ('django.db.models.fields.CharField', [], {'max_length': "'100'"})
        },
        u'farmacias.farmacia': {
            'Meta': {'ordering': "['-nombre']", 'object_name': 'Farmacia'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': "'200'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'latitud': ('django.db.models.fields.CharField', [], {'max_length': "'50'", 'null': 'True', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.CharField', [], {'max_length': "'50'", 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "'Tipo 1'", 'max_length': "'10'"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'farmacias.medicamentos': {
            'Meta': {'object_name': 'Medicamentos'},
            'estado': ('django.db.models.fields.BooleanField', [], {}),
            'farmacia': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['farmacias.Farmacia']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industria': ('django.db.models.fields.CharField', [], {'max_length': "'50'"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'stock': ('django.db.models.fields.IntegerField', [], {})
        },
        u'farmacias.pais': {
            'Meta': {'object_name': 'Pais'},
            'farmacia': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['farmacias.Farmacia']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': "'50'"})
        },
        u'farmacias.turno': {
            'Meta': {'object_name': 'Turno'},
            'farmacia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['farmacias.Farmacia']", 'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['farmacias']