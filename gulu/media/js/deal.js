/**
 * Gulu Deal js
 * 
 * @author Jason Ke <jason.ke@geniecapital.com>
 */

/* Gulu Deal module JS */
Deal = {}
Deal._config = {
		'restaurant_deal_container': null,
		'deal_prev': null,
		'deal_next': null,
};

Deal.init = function(_user_config) {
	// extend the default config with the user's config
	$.extend(Deal._config, _user_config);
}

//Use the ajax to swap between deal pages
Deal.updateDealView = function(container, deal_id){
	
	url = '/deal/ajax/deal_view_single';
	container.children().fadeOut('fast', function(){
			container.children().remove();
			$.ajax({
			   type: "POST",
			   dataType: "html",
			   url: url,
			   data: {
				   'deal_id':deal_id,
			   },
			   success: function(data) {
					ctn = $(Deal._config['restaurant_deal_container']);
					ctn.prepend(data);
					ctn.children().hide();
					ctn.children().fadeIn();
					/*
					var comment = new GComments.Commenter({
						container : $(Deal._config['Deal_comments']).first(),
					});
					*/
			   }
			});
		}
	);
	
	/*
	restaurant_id = form_data.find(Deal._config['restaurant_id']).val();
	user_id = form_data.find(Deal._config['user_id']).val();
	dish_id = form_data.find(Deal._config['dish_id']).val();
	content = form_data.find(Deal._config['Deal_content_input']).val();
	*/
	
}