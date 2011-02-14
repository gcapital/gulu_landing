/**
 * Gulu Restaurant picker JS widget 
 *
 * Attaches to a text input, container div, reset button, and hidden input.  Adds
 * autocomplete restaurant selection to the text input, updates the container div 
 * with restaurant details, and saves the restaurant id to the hidden input.
 *
 * @author Ben Homnick <bhomnick@gmail.com
 */

var Restaurant = Restaurant || {};

Restaurant.RestaurantPicker = function(config){
	this._config = {
		container: null,	// jQuery selector of container to hold restaurant details
		input: null,		// jQuery selector of input where selected restaurant_id is stored
		search: null,		// jQuery selector of search autocomplete input
		reset: null,		// jQuery selector of reset button
	};
	$.extend(this._config, config);
	
	// Add an autocomplete to the search input
	this._config.search.autocomplete({
		source: "/restaurant/ajax/search-restaurants",
		minLength: 2,
		select: $.proxy(this._handleAutocomplete, this),
	});
	
	// Add bind to reset button
	this._config.reset.live('click', $.proxy(this._reset, this));

	// Load initial data
	default_data = this._config.input.val();
	if(default_data != null && default_data != ""){
		this._chooseRestaurant(default_data);
	}
};
	
Restaurant.RestaurantPicker.prototype = {
	_reset: function(){
		this._config.reset.fadeOut();
		this._config.search.fadeIn();
		this._config.search.val("");
		this._config.container.fadeOut();
		this._config.input.val("");
	},
	_chooseRestaurant: function(rid){
		url = "/restaurant/ajax/get-restaurant-details?rid=" + rid;
		this._config.search.hide();
		this._config.reset.fadeIn();
		this._config.input.val(rid);
		this._config.container.load(url).fadeIn('slow');
	},
	_handleAutocomplete: function(event, ui){
		this._chooseRestaurant(ui.item.id);
	},
};
