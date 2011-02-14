# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Nonce.token_key'
        db.alter_column('piston_nonce', 'token_key', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Nonce.consumer_key'
        db.alter_column('piston_nonce', 'consumer_key', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Consumer.secret'
        db.alter_column('piston_consumer', 'secret', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Consumer.key'
        db.alter_column('piston_consumer', 'key', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Site.secret'
        db.alter_column('piston_site', 'secret', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Site.key'
        db.alter_column('piston_site', 'key', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Site.api_key'
        db.alter_column('piston_site', 'api_key', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Token.secret'
        db.alter_column('piston_token', 'secret', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Token.verifier'
        db.alter_column('piston_token', 'verifier', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Token.key'
        db.alter_column('piston_token', 'key', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Sync.verifier'
        db.alter_column('piston_sync', 'verifier', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Sync.token'
        db.alter_column('piston_sync', 'token', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Sync.token_secret'
        db.alter_column('piston_sync', 'token_secret', self.gf('django.db.models.fields.CharField')(max_length=100))


    def backwards(self, orm):
        
        # Changing field 'Nonce.token_key'
        db.alter_column('piston_nonce', 'token_key', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Nonce.consumer_key'
        db.alter_column('piston_nonce', 'consumer_key', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Consumer.secret'
        db.alter_column('piston_consumer', 'secret', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Consumer.key'
        db.alter_column('piston_consumer', 'key', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Site.secret'
        db.alter_column('piston_site', 'secret', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Site.key'
        db.alter_column('piston_site', 'key', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Site.api_key'
        db.alter_column('piston_site', 'api_key', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Token.secret'
        db.alter_column('piston_token', 'secret', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Token.verifier'
        db.alter_column('piston_token', 'verifier', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Token.key'
        db.alter_column('piston_token', 'key', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Sync.verifier'
        db.alter_column('piston_sync', 'verifier', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Sync.token'
        db.alter_column('piston_sync', 'token', self.gf('django.db.models.fields.CharField')(max_length=30))

        # Changing field 'Sync.token_secret'
        db.alter_column('piston_sync', 'token_secret', self.gf('django.db.models.fields.CharField')(max_length=50))


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'photos.photo': {
            'Meta': {'ordering': "['content_type', 'object_id', 'order']", 'object_name': 'Photo'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_main': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'restaurant_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user_profiles.UserProfile']", 'null': 'True', 'blank': 'True'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'piston.consumer': {
            'Meta': {'object_name': 'Consumer'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'pending'", 'max_length': '16'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'consumers'", 'null': 'True', 'to': "orm['auth.User']"})
        },
        'piston.nonce': {
            'Meta': {'object_name': 'Nonce'},
            'consumer_key': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'token_key': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'piston.site': {
            'Meta': {'object_name': 'Site'},
            'access_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'api_key': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'authorize_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'request_url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'piston.sync': {
            'Meta': {'object_name': 'Sync'},
            'callback': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_access': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['piston.Site']"}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'token_secret': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user_profiles.UserProfile']"}),
            'verifier': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'piston.token': {
            'Meta': {'object_name': 'Token'},
            'callback': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'callback_confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'consumer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['piston.Consumer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'timestamp': ('django.db.models.fields.IntegerField', [], {'default': '1296444831L'}),
            'token_type': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tokens'", 'null': 'True', 'to': "orm['auth.User']"}),
            'verifier': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'user_profiles.userprofile': {
            'Meta': {'object_name': 'UserProfile', '_ormbases': ['auth.User']},
            'about_me': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'favorite_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'follower_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'following_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'gender': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gulu_points': ('django.db.models.fields.FloatField', [], {'default': '5'}),
            'main_profile_pic': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'user_main_profile_pic'", 'null': 'True', 'to': "orm['photos.Photo']"}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'phone_country': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True'}),
            'profile_pics': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_profile_pics'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['photos.Photo']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['piston']
