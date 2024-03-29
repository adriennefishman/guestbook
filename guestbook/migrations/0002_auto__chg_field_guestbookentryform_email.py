# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'GuestbookEntryForm.email'
        db.alter_column('guestbook_guestbookentryform', 'email', self.gf('django.db.models.fields.EmailField')(max_length=50))

    def backwards(self, orm):

        # Changing field 'GuestbookEntryForm.email'
        db.alter_column('guestbook_guestbookentryform', 'email', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        'guestbook.guestbookentryform': {
            'Meta': {'object_name': 'GuestbookEntryForm'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['guestbook']