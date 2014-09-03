# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GuestbookEntryForm'
        db.create_table('guestbook_guestbookentryform', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('guestbook', ['GuestbookEntryForm'])


    def backwards(self, orm):
        # Deleting model 'GuestbookEntryForm'
        db.delete_table('guestbook_guestbookentryform')


    models = {
        'guestbook.guestbookentryform': {
            'Meta': {'object_name': 'GuestbookEntryForm'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['guestbook']