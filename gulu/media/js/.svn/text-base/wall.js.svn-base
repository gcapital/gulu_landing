/*
 * Gulu Wall module JS
 *
 */

var Wall = {};

/*
 * Ajax wall post widget
 *
 */
Wall.Poster = function(config){	
	this._config = {
		form: null,	// jQuery selector of form
		container: null, // jQuery selector of activity feed container
	}
	$.extend(this._config, config);
	this._config.form.find("#id_content").autogrow();
	this._config.form.find("#id_content").click(function(){
		this.value=(this.value=='comments')?'':this.value;
	});
	this._config.form.find("#id_content").blur(function(){
		this.value=!this.value?'comments':this.value;
	});
	submit = this._config.form.find("#wall_submit");
	submit.live('click', $.proxy(this._submit, this));
};

Wall.Poster.prototype = {
	_submit: function() {
		data = this._config.form.serialize()
		$.ajax({
			type: "POST",
			dataType: "json",
			url: "/wall/ajax/post/",
			data: data,
			success: $.proxy(this._handleSuccess, this),
		});
	},
	_handleSuccess: function(response){
		if(response.status == 0){
			this._config.container.prepend(response.html).hide().fadeIn('slow');
		}
	},
};
