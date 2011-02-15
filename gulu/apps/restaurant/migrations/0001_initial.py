# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Restaurant'
        db.create_table('restaurant_restaurant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(db_index=True, max_length=100, unique=True, null=True, blank=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('region', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurant.RestaurantType'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('business_hours', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('transportation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('note', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('score', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('can_upload_dish', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('rating_food', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rating_atmosphere', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rating_service', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rating_price', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('follower_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('count_recommend', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('restaurant', ['Restaurant'])

        # Adding M2M table for field services on 'Restaurant'
        db.create_table('restaurant_restaurant_services', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('restaurant', models.ForeignKey(orm['restaurant.restaurant'], null=False)),
            ('restaurantservice', models.ForeignKey(orm['restaurant.restaurantservice'], null=False))
        ))
        db.create_unique('restaurant_restaurant_services', ['restaurant_id', 'restaurantservice_id'])

        # Adding M2M table for field best_reviews on 'Restaurant'
        db.create_table('restaurant_restaurant_best_reviews', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('restaurant', models.ForeignKey(orm['restaurant.restaurant'], null=False)),
            ('review', models.ForeignKey(orm['review.review'], null=False))
        ))
        db.create_unique('restaurant_restaurant_best_reviews', ['restaurant_id', 'review_id'])

        # Adding M2M table for field managers on 'Restaurant'
        db.create_table('restaurant_restaurant_managers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('restaurant', models.ForeignKey(orm['restaurant.restaurant'], null=False)),
            ('userprofile', models.ForeignKey(orm['user_profiles.userprofile'], null=False))
        ))
        db.create_unique('restaurant_restaurant_managers', ['restaurant_id', 'userprofile_id'])

        # Adding model 'RestaurantService'
        db.create_table('restaurant_restaurantservice', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('restaurant', ['RestaurantService'])

        # Adding model 'RestaurantRating'
        db.create_table('restaurant_restaurantrating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['user_profiles.UserProfile'])),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurant.Restaurant'])),
            ('is_delicious', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('good_atmosphere', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('good_service', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('good_price', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ip_address', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('restaurant', ['RestaurantRating'])

        # Adding model 'Vip'
        db.create_table('restaurant_vip', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurant.Restaurant'])),
            ('reserve', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('delivery', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('delivery_free', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('takeout', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order_online_dis', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order_online_dis_v', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('restaurant_dis', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('restaurant_dis_v', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('reserve_online_dis', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('reserve_online_dis_v', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('other', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('other_description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('price_1m', self.gf('django.db.models.fields.FloatField')()),
            ('price_3m', self.gf('django.db.models.fields.FloatField')()),
            ('price_6m', self.gf('django.db.models.fields.FloatField')()),
            ('price_12m', self.gf('django.db.models.fields.FloatField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('restaurant', ['Vip'])

        # Adding model 'RestaurantType'
        db.create_table('restaurant_restauranttype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal('restaurant', ['RestaurantType'])

        # Adding model 'Chef'
        db.create_table('restaurant_chef', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['restaurant.Restaurant'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('priority', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('restaurant', ['Chef'])


    def backwards(self, orm):
        
        # Deleting model 'Restaurant'
        db.delete_table('restaurant_restaurant')

        # Removing M2M table for field services on 'Restaurant'
        db.delete_table('restaurant_restaurant_services')

        # Removing M2M table for field best_reviews on 'Restaurant'
        db.delete_table('restaurant_restaurant_best_reviews')

        # Removing M2M table for field managers on 'Restaurant'
        db.delete_table('restaurant_restaurant_managers')

        # Deleting model 'RestaurantService'
        db.delete_table('restaurant_restaurantservice')

        # Deleting model 'RestaurantRating'
        db.delete_table('restaurant_restaurantrating')

        # Deleting model 'Vip'
        db.delete_table('restaurant_vip')

        # Deleting model 'RestaurantType'
        db.delete_table('restaurant_restauranttype')

        # Deleting model 'Chef'
        db.delete_table('restaurant_chef')


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
        'restaurant.chef': {
            'Meta': {'object_name': 'Chef'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'priority': ('django.db.models.fields.SmallIntegerField', [], {}),
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
        'restaurant.restaurantrating': {
            'Meta': {'object_name': 'RestaurantRating'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'good_atmosphere': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'good_price': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'good_service': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'is_delicious': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['restaurant.Restaurant']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user_profiles.UserProfile']"})
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
        'restaurant.vip': {
            'Meta': {'object_name': 'Vip'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'delivery': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'delivery_free': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_online_dis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order_online_dis_v': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'other': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'other_description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price_12m': ('django.db.models.fields.FloatField', [], {}),
            'price_1m': ('django.db.models.fields.FloatField', [], {}),
            'price_3m': ('django.db.models.fields.FloatField', [], {}),
            'price_6m': ('django.db.models.fields.FloatField', [], {}),
            'reserve': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reserve_online_dis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'reserve_online_dis_v': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['restaurant.Restaurant']"}),
            'restaurant_dis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'restaurant_dis_v': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'takeout': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
        }
    }

    complete_apps = ['restaurant']
