# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Deal.end_date'
        db.delete_column('deal_deal', 'end_date')

        # Deleting field 'Deal.start_date'
        db.delete_column('deal_deal', 'start_date')

        # Adding field 'Deal.start_datetime'
        db.add_column('deal_deal', 'start_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2011, 1, 21)), keep_default=False)

        # Adding field 'Deal.end_datetime'
        db.add_column('deal_deal', 'end_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2011, 1, 21)), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Deal.end_date'
        db.add_column('deal_deal', 'end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)

        # Adding field 'Deal.start_date'
        db.add_column('deal_deal', 'start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)

        # Deleting field 'Deal.start_datetime'
        db.delete_column('deal_deal', 'start_datetime')

        # Deleting field 'Deal.end_datetime'
        db.delete_column('deal_deal', 'end_datetime')


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
        'deal.deal': {
            'Meta': {'object_name': 'Deal'},
            'amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'conditions': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cover': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Photo']", 'null': 'True', 'blank': 'True'}),
            'dish': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dish.Dish']", 'null': 'True', 'blank': 'True'}),
            'end_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ongoing': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'deals'", 'to': "orm['restaurant.Restaurant']"}),
            'start_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['user_profiles.UserProfile']"})
        },
        'dish.dish': {
            'Meta': {'object_name': 'Dish'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'count_recommend': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'dish_pics': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'dish_dish_related_dish'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['photos.Photo']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'main_pic': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'dish_dish_main_pic_dish'", 'null': 'True', 'to': "orm['photos.Photo']"}),
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
            'main_profile_pic': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'restaurant_profile_pic'", 'null': 'True', 'to': "orm['photos.Photo']"}),
            'managers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['user_profiles.UserProfile']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'note': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'profile_pics': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'restaurant_profile_pics'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['photos.Photo']"}),
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
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'dish': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dish.Dish']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photo_related_review'", 'null': 'True', 'to': "orm['photos.Photo']"}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['restaurant.Restaurant']"}),
            'total_comment': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
            'main_profile_pic': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'user_main_profile_pic'", 'null': 'True', 'to': "orm['photos.Photo']"}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'profile_pics': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'user_profile_pics'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['photos.Photo']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['deal']