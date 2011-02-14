/**
 * Gulu Dish js
 * 
 * 
 * @author Gage Tseng <gage.tseng@geniecapital.com>
 */

Dish = {};

Dish.DishOrderInput = function(config) {
	/* 
	 *  add/minus action of dish order unmber
	 */
	
	this._config = {
		add: null,			// jQuery selector of button to increase order number
		minus: null,		// jQuery selector of button to decrease order number
		input: null,	// jQuery selector of text input to show order number
	};
	$.extend(this._config, config);
	
	// Load initial data
	default_data = this._config.input.val();
	
	// Add an increase event to the add button
	this._config.add.live('click', $.proxy(this._increase,this));
	
	// Add an decrease event to the minus button
	this._config.minus.live('click', $.proxy(this._decrease, this));
};

Dish.DishOrderInput.prototype = {
	_increase: function(){
		var order_num = parseInt(this._config.input.val());
		if(order_num<0)
			this._config.input.val(0);
		else if(order_num>=99)
			this._config.input.val(99);
		else
			this._config.input.val(order_num+1);
	},
	_decrease: function(){
		var order_num = parseInt(this._config.input.val());
		if(order_num<=0)
			this._config.input.val(0);
		else if(order_num>99)
			this._config.input.val(99);
		else
			this._config.input.val(order_num-1);
	},
};

Dish.MenuFilter = function(config) {
	/* 
	 *  display menu by given specific dish type
	 */
	
	this._config = {
		filter: null,		// jQuery selector of select input to filter dish type
		menu: null,			// jQuery selector of display menu
		restaurant: null    // restaurant id (integer)
	};
	$.extend(this._config, config);
	
	this._change_type = function(){
		url = '/dish/ajax/show_menu';
		dish_type = this._config.filter.val();
		menu = this._config.menu;
		$.ajax({
		   type: "GET",
		   dataType: "html",
		   url: url,
		   data: {
			   'restaurant_id' : this._config.restaurant,
			   'dish_type' : dish_type,
		   },
		   success: function(data) {
			   menu.html(data);
		   }
		});
	};
	
	this._config.filter.change($.proxy(this._change_type, this));
}

/**
 * Dish picker widget
 */
Dish.DishPicker = function(config){
	this._config = {
		container: null,	// jQuery selector of container to hold restaurant details
		input: null,		// jQuery selector of input where selected restaurant_id is stored
		search: null,		// jQuery selector of search autocomplete input
		reset: null,		// jQuery selector of reset button
		restaurant_id: null,// Restaurant id of dishes to search
	};
	$.extend(this._config, config);
	
	// Add an autocomplete to the search input
	this._config.search.autocomplete({
		source: "/dish/ajax/search/" + this._config.restaurant_id + "/",
		minLength: 1,
		select: $.proxy(this._handleAutocomplete, this),
	});
	
	// Add bind to reset button
	this._config.reset.live('click', $.proxy(this._reset, this));

	// Load initial data
	default_data = this._config.input.val();
	if(default_data != null && default_data != ""){
		this._chooseDish(default_data);
	}
};
	
Dish.DishPicker.prototype = {
	_reset: function(){
		this._config.reset.fadeOut();
		this._config.search.fadeIn();
		this._config.search.val("");
		this._config.container.fadeOut();
		this._config.input.val("");
	},
	_chooseDish: function(did){
		url = "/dish/ajax/get-details?did=" + did;
		this._config.search.hide();
		this._config.reset.fadeIn();
		this._config.input.val(did);
		this._config.container.load(url).fadeIn('slow');
	},
	_handleAutocomplete: function(event, ui){
		this._chooseDish(ui.item.id);
	},
};
