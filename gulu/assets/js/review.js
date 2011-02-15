/**
 * Gulu Review js
 * 
 * @author Jason Ke <jason.ke@geniecapital.com>
 */

/* Gulu Review module JS */
Review = {}

Review.Post = function(config) {
	// extend the default config with the user's config
	this._config = {
		'all_reviews_container': null,
		'review_submit': null,
		'review_form': null,
	};
	$.extend(this._config, config);
	this._config.review_form.find('#id_content').autogrow();
	this._config.review_submit.live('click', $.proxy(this._addReview,this));	
}

Review.Post.prototype = {
	_addReview : function(){
		form = this._config.review_form;
		url = '/review/ajax/review_display_added_post';
		restaurant_id = form.find('#id_restaurant').val();
		user_id = form.find('#id_user').val();
		dish_id = form.find('#id_dish').val();
		content = form.find('#id_content').val();
		photo_id = form.find('#id_photo_id').val();
		photo_url = form.find('#id_photo_url').val();
		
		if(content=='') {
			var msg = 'Please type some text for the review.';
			this._showError(msg);
			return 0;
		}
		
		if(restaurant_id=='' || user_id=='') {
			var msg = 'There are some errors, please make sure you are writing review in right place.';
			this._showError(msg);
			return 1;
		}
		
		reviews_container = this._config.all_reviews_container;
		
		$.ajax({
		   type: "POST",
		   dataType: "json",
		   url: url,
		   data: {
			   'restaurant': restaurant_id,
			   'user':user_id,
			   'dish':dish_id,
			   'content': content,
			   'photo_id': photo_id,
			   'photo_url': photo_url,
		   },
		   success: function(data) {
			   if(data.status == 1) {
				   var new_review = $(data.html);
				   reviews_container.prepend(new_review.hide().slideDown());
				   
				   var comment = new GComments.Commenter({
					   container : new_review.find('.review_comments'),
				   });
				   
				   // clean the form
				   form.find('#id_dish').val('');
				   form.find('#id_content').val('');
				   form.find('#id_photo_id').val('');
				   form.find('#id_photo_url').val('');
				   form.find('#img_placeholder img').remove();
			   }
			   else{
				   var oMsg = $('<div class="emsg">'+data.msg+'</div>');
				   $('#form_error_msg').html(oMsg.hide().fadeIn(1000).fadeOut(10000));
			   }
		   }
		});
	},
	
	_showError : function(msg) {
		var oMsg = $('<div class="emsg">'+msg+'</div>');
		$('#form_error_msg').html(oMsg.hide().fadeIn(1000).fadeOut(5000));
	}
};

Review.more={
	__button_id:null,
	init:function(_button_id) {
		Review.more.__button_id=_button_id;
		$(Review.more.__button_id).mouseup(function() {
			        $.ajax({
				                type:"POST",
				                dataType:"json",
				                url:"/review/ajax/review_more/",
				                data:{
					                'owner':$(Review.more.__button_id).attr('_owner'),
					                'sid':$(Review.more.__button_id).prev().attr('_sid')
				                },
				                success:Review.more.display
			                });
		        });
	},
	display:function(data) {
		if(data.html) $(Review.more.__button_id).before(data.html);
		if(!data.more) $(Review.more.__button_id).remove();
	}
}