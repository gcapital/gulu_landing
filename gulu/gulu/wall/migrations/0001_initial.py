# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'RestaurantWall'
        db.create_table('wall_restaurantwall', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poster', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wall_restaurantwall_related', to=orm['user_profiles.UserProfile'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('total_comment', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('post_from', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(default=None, max_length=15)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 1, 12, 14, 17, 30, 59024))),
            ('update_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 1, 12, 14, 17, 30, 59060))),
            ('action', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurant.Restaurant'])),
        ))
        db.send_create_signal('wall', ['RestaurantWall'])

        # Adding model 'UserWall'
        db.create_table('wall_userwall', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poster', self.gf('django.db.models.fields.related.ForeignKey')(related_name='wall_userwall_related', to=orm['user_profiles.UserProfile'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('total_comment', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('post_from', self.gf('django.db.models.fields.SmallIntegerField')(default=0)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(default=None, max_length=15)),
            ('create_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 1, 12, 14, 17, 30, 59024))),
            ('update_time', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 1, 12, 14, 17, 30, 59060))),
            ('action', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_wall_owner', to=orm['user_profiles.UserProfile'])),
        ))
        db.send_create_signal('wall', ['UserWall'])


    def backwards(self, orm):
        
        # Deleting model 'RestaurantWall'
        db.delete_table('wall_restaurantwall')

        # Deleting model 'UserWall'
        db.delete_table('wall_userwall')


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
        'dish.dish': {
            'Meta': {'object_name': 'Dish'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'count_recommend': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'points': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reserve': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dishes'", 'to': "orm['restaurant.Restaurant']"}),
            'sale_out': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'special': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'total_reserve': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dish.DishType']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user_profiles.UserProfile']"}),
            'vip_price': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        'dish.dishtype': {
            'Meta': {'object_name': 'DishType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['restaurant.Restaurant']"})
        },
        'restaurant.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'best_reviews': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'restaurant_best_reviews'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['review.Review']"}),
            'business_hours': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'can_upload_dish': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'count_recommend': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'follower_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'managers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['user_profiles.UserProfile']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'rating_atmosphere': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rating_food': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rating_price': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rating_service': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'score': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['restaurant.RestaurantService']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'transportation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['restaurant.RestaurantType']"})
        },
        'restaurant.restaurantservice': {
            'Meta': {'object_name': 'RestaurantService'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'restaurant.restauranttype': {
            'Meta': {'object_name': 'RestaurantType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        'review.review': {
            'Meta': {'object_name': 'Review'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'dish': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dish.Dish']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['restaurant.Restaurant']"}),
            'time_stamp': ('django.db.models.fields.TimeField', [], {'auto_now_add': 'True'}),
            'total_comment': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user_profiles.UserProfile']"})
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
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        'wall.restaurantwall': {
            'Meta': {'object_name': 'RestaurantWall'},
            'action': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 1, 12, 14, 17, 30, 59024)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'default': 'None', 'max_length': '15'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['restaurant.Restaurant']"}),
            'post_from': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'poster': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wall_restaurantwall_related'", 'to': "orm['user_profiles.UserProfile']"}),
            'total_comment': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'update_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 1, 12, 14, 17, 30, 59060)'})
        },
        'wall.userwall': {
            'Meta': {'object_name': 'UserWall'},
            'action': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'create_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 1, 12, 14, 17, 30, 59024)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'default': 'None', 'max_length': '15'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_wall_owner'", 'to': "orm['user_profiles.UserProfile']"}),
            'post_from': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'poster': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wall_userwall_related'", 'to': "orm['user_profiles.UserProfile']"}),
            'total_comment': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'update_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 1, 12, 14, 17, 30, 59060)'})
        }
    }

    complete_apps = ['wall']
