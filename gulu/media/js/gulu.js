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
		input: null,		// jQuery selector of input where date/time are saved
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
	},	
};

Gulu.Like = {
	likeit : function(btn, content_type_id, object_id, user_id){
		var btn_class = btn.attr('class');
		var like_type = btn_class.substring(0,btn_class.indexOf('_btn'))
		var url = '/like/'+like_type+'/'+content_type_id+'/'+object_id;
		$.ajax({
		   type: "GET",
		   dataType: "json",
		   url: url,
		   success: function(data) {
			   if(data.type=='1')
				   $('.'+user_id+'_'+content_type_id+'_'+object_id+'_like .like_btn').attr('class','unlike_btn');
			   else if(data.type=='0')
				   $('.'+user_id+'_'+content_type_id+'_'+object_id+'_like .unlike_btn').attr('class','like_btn');
			   $('.'+user_id+'_'+content_type_id+'_'+object_id+'_like .like_info_wrap').html(data.like_info)
		   }
		});
	},
}
