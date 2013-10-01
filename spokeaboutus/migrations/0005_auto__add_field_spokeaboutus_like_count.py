# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SpokeAboutUs.like_count'
        db.add_column(u'spokeaboutus_spokeaboutus', 'like_count',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SpokeAboutUs.like_count'
        db.delete_column(u'spokeaboutus_spokeaboutus', 'like_count')


    models = {
        u'spokeaboutus.spokeaboutus': {
            'Meta': {'ordering': "('order',)", 'object_name': 'SpokeAboutUs'},
            'about_us': ('django.db.models.fields.TextField', [], {}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'like_count': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'spoke_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'spoke_link': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
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