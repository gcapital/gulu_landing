# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'RestaurantWall'
        db.delete_table('wall_restaurantwall')

        # Deleting model 'UserWall'
        db.delete_table('wall_userwall')

        # Adding model 'WallPost'
        db.create_table('wall_wallpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poster', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user_profiles.UserProfile'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photos.Photo'], null=True, blank=True)),
            ('owner_content_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='owner', to=orm['contenttypes.ContentType'])),
            ('owner_object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('wall', ['WallPost'])


    def backwards(self, orm):
        
        # Adding model 'RestaurantWall'
        db.create_table('wall_restaurantwall', (
            ('update_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 1, 25, 21, 42, 22, 453750))),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photos.Photo'], null=True, blank=True)),
            ('poster', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wall_restaurantwall_related', to=orm['user_profiles.UserProfile'])),
            ('post_from', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 1, 25, 21, 42, 22, 453704))),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurant.Restaurant'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('total_comment', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(default=None, max_length=15)),
            ('action', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('wall', ['RestaurantWall'])

        # Adding model 'UserWall'
        db.create_table('wall_userwall', (
            ('update_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 1, 25, 21, 42, 22, 453750))),
            ('photo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photos.Photo'], null=True, blank=True)),
            ('poster', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wall_userwall_related', to=orm['user_profiles.UserProfile'])),
            ('post_from', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 1, 25, 21, 42, 22, 453704))),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_wall_owner', to=orm['user_profiles.UserProfile'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('total_comment', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(default=None, max_length=15)),
            ('action', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('wall', ['UserWall'])

        # Deleting model 'WallPost'
        db.delete_table('wall_wallpost')


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
            'profile_pics': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_profile_pics'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['photos.Photo']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'wall.wallpost': {
            'Meta': {'ordering': "['-created']", 'object_name': 'WallPost'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner_content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owner'", 'to': "orm['contenttypes.ContentType']"}),
            'owner_object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Photo']", 'null': 'True', 'blank': 'True'}),
            'poster': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user_profiles.UserProfile']"})
        }
    }

    complete_apps = ['wall']