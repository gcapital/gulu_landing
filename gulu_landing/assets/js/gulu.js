/**
 * Gulu Date/time picker JS widget
 *
 * Creates date and time input fields and saves combined datetime to a hidden
 * input field.  Requires jQuery UI and Trent Richardson's timepicker addon
 * <http://trentrichardson.com/examples/timepicker/>
 *
 * @author Ben Homnick <bhomnick@gmail.com>
 */

var Gulu = Gulu || {};

Gulu.DateTimePicker = function(config){
	this._config = {
		container: null,	// jQuery selector of container to hold picker
		input: null		// jQuery selector of input where date/time are saved
	};
	$.extend(this._config, config);
	
	var template = '<div class="gulu_datetimepicker_date">' + 
		'<input type="text" class="gulu_datetimepicker_date_input" value="yyyy-mm-dd" />' + 
		'</div><!-- .gulu_datetimepicker_date -->' + 
		'<input type="text" class="gulu_datetimepicker_time_input input_text" value="00:00" />';
	
	this._config.container.html(template);
	
	// Intialize the jQuery UI elements
	this._config.container.find(".gulu_datetimepicker_date_input").datepicker({
		showOn: 'button',
		buttonImage: "/media/images/btn_calendar.png",
		buttonImageOnly: false,
		dateFormat: 'yy-mm-dd'	//format definition can be found at http://docs.jquery.com/UI/Datepicker/formatDate
	});
	//this._config.container.find(".gulu_datetimepicker_time_input").timepicker({ });
	
	// Create update bind, using $.proxy to make sure the 'this' context is preserved in
	// the callback function.  Otherwise, jQuery sets 'this' to the selector the bind is
	// attached to.
	this._config.container.find(".gulu_datetimepicker_time_input, .gulu_datetimepicker_date_input").change($.proxy(this._update, this));

	// Load initial data
	default_data = this._config.input.val();
	if(default_data != null && default_data != ""){
		default_data = default_data.split(" ");
		this._config.container.find(".gulu_datetimepicker_date_input").val(default_data[0]);
		this._config.container.find(".gulu_datetimepicker_time_input").val(default_data[1]);
	}
};

Gulu.DateTimePicker.prototype = {
	_update: function(){
		var datetime = 
			this._config.container.find(".gulu_datetimepicker_date_input").val() + " " + 
			this._config.container.find(".gulu_datetimepicker_time_input").val();
		this._config.input.val(datetime);
	}
};


// returns the value of the url parameter name
Gulu.getUrlParameter = function(name) {
	name = name.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
	var regex = new RegExp("[\\?&]"+name+"=([^&#]*)");
	var result = regex.exec(window.location.href);
	if(result == null) {
		return "";
	}
	else {
		return result[1];
	}
};

// redirects the browser to url
Gulu.redirect = function(url) {
	window.location = url;
};

// input element which contains a default value and clears on focus
Gulu.DefaultValueField = function(element, defaultValue){

    if(element.attr('type')=='password'){
        element.hide();
        var clear_input = $('<input type="text" value="'+defaultValue+'" class="'+element.attr('class')+' clear">');
        clear_input.attr('tabindex', element.attr('tabindex'));
        clear_input.insertAfter(element);
        clear_input.click(doFocusPassword);
        clear_input.focus(doFocusPassword);
    }else{
        element.val(defaultValue);
        element.click(doFocus);
        element.focus(doFocus);
        element.blur(function() {
            if($(this).val() == ""){
                $(this).val(defaultValue);
            }
        });
    }
    
    function doFocusPassword() {
        element.next().hide();
        element.show();
        element.val('');
        element.focus();
        element.blur(function() {
            if($(this).val() == ""){
                $(this).parent().find('.clear').val(defaultValue).show();
                $(this).hide();
            }
        });
    };
    
    function doFocus() {
        var v = $(this).val();
        $(this).val((v == defaultValue) ? "" : v);
    };
};

// preload
Gulu.Preload = function(images){
    var preload = [];
    for(var key in images){
        if(key != 'contains'){
            var img_obj = $('<img>').attr('src', images[key]);
            preload.push(img_obj);
        }
    }
}

