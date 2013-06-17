# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SpokeAboutUs.spoke_source_uid'
        db.add_column(u'spokeaboutus_spokeaboutus', 'spoke_source_uid',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Deleting field 'SpokeSource.name'
        db.delete_column(u'spokeaboutus_spokesource', 'name')

        # Deleting field 'SpokeSource.icon'
        db.delete_column(u'spokeaboutus_spokesource', 'icon')

        # Adding field 'SpokeSource.spoke_source'
        db.add_column(u'spokeaboutus_spokesource', 'spoke_source',
                      self.gf('django.db.models.fields.CharField')(default=('twitter', 'Twitter'), max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SpokeSource.limit'
        db.add_column(u'spokeaboutus_spokesource', 'limit',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'SpokeSource.search_query'
        db.add_column(u'spokeaboutus_spokesource', 'search_query',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'SpokeSource.periodicity'
        db.add_column(u'spokeaboutus_spokesource', 'periodicity',
                      self.gf('django.db.models.fields.IntegerField')(default=60),
                      keep_default=False)

        # Adding field 'SpokeSource.updated'
        db.add_column(u'spokeaboutus_spokesource', 'updated',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SpokeAboutUs.spoke_source_uid'
        db.delete_column(u'spokeaboutus_spokeaboutus', 'spoke_source_uid')


        # User chose to not deal with backwards NULL issues for 'SpokeSource.name'
        raise RuntimeError("Cannot reverse this migration. 'SpokeSource.name' and its values cannot be restored.")
        # Adding field 'SpokeSource.icon'
        db.add_column(u'spokeaboutus_spokesource', 'icon',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'SpokeSource.spoke_source'
        db.delete_column(u'spokeaboutus_spokesource', 'spoke_source')

        # Deleting field 'SpokeSource.limit'
        db.delete_column(u'spokeaboutus_spokesource', 'limit')

        # Deleting field 'SpokeSource.search_query'
        db.delete_column(u'spokeaboutus_spokesource', 'search_query')

        # Deleting field 'SpokeSource.periodicity'
        db.delete_column(u'spokeaboutus_spokesource', 'periodicity')

        # Deleting field 'SpokeSource.updated'
        db.delete_column(u'spokeaboutus_spokesource', 'updated')


    models = {
        u'spokeaboutus.spokeaboutus': {
            'Meta': {'ordering': "('order',)", 'object_name': 'SpokeAboutUs'},
            'about_us': ('django.db.models.fields.TextField', [], {}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'spoke_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'spoke_source': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['spokeaboutus.SpokeSource']"}),
            'spoke_source_uid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'spokeaboutus.spokesource': {
            'Meta': {'object_name': 'SpokeSource'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'limit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'periodicity': ('django.db.models.fields.IntegerField', [], {'default': '60'}),
            'search_query': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'spoke_source': ('django.db.models.fields.CharField', [], {'default': "('twitter', 'Twitter')", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['spokeaboutus']