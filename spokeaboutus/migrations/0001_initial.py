# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SpokeSource'
        db.create_table(u'spokeaboutus_spokesource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('icon', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'spokeaboutus', ['SpokeSource'])

        # Adding model 'SpokeAboutUs'
        db.create_table(u'spokeaboutus_spokeaboutus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('about_us', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('spoke_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('spoke_source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['spokeaboutus.SpokeSource'])),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'spokeaboutus', ['SpokeAboutUs'])


    def backwards(self, orm):
        # Deleting model 'SpokeSource'
        db.delete_table(u'spokeaboutus_spokesource')

        # Deleting model 'SpokeAboutUs'
        db.delete_table(u'spokeaboutus_spokeaboutus')


    models = {
        u'spokeaboutus.spokeaboutus': {
            'Meta': {'object_name': 'SpokeAboutUs'},
            'about_us': ('django.db.models.fields.TextField', [], {}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'spoke_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'spoke_source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['spokeaboutus.SpokeSource']"})
        },
        u'spokeaboutus.spokesource': {
            'Meta': {'object_name': 'SpokeSource'},
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['spokeaboutus']