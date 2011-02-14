/**
 * Gulu gcomments module js
 *
 * @author Ben Homnick <bhomnick@gmail.com>
 */

var GComments = GComments || {};

/**
 * Gulu Commenter
 *
 * Front-end for AJAX comment posting through Django's built-in comment
 * app.  Based on Brandon Konkle's django-ajaxcomments <ttp://bitbucket.org/bkonkle/django-ajaxcomments/>
 */
GComments.Commenter = function(config){
	this._textarea = null;
	this._post_button = null;
	this._form = null;
	this._config = {
		container: null,	// jQuery selector of container to hold comments
		max_length: 210,	// Maximum number of characters allowed
		placeholder: "comments",	// Textarea placeholder text
	};
	
	$.extend(this._config, config);

	this._textarea = this._config.container.find("textarea");
	this._post_button = this._config.container.find(".btn_post");
	this._form = this._config.container.find("form");
	
	this._form.submit($.proxy(function() {
		this._postComment();
		return false;
	}, this));
	
	this._textarea.val(this._config.placeholder);
	this._textarea.click($.proxy(this._clickTextarea, this));
	this._textarea.blur($.proxy(this._blurTextarea, this));
	this._textarea.change($.proxy(this._handleOverflow, this));
	this._textarea.keypress($.proxy(this._handleOverflow, this));
	this._textarea.bind('input paste', $.proxy(this._handleOverflow, this));
};
	
GComments.Commenter.prototype = {
	_clickTextarea: function(){
		this._textarea.val((this._textarea.val() == this._config.placeholder) ? "" : this._textarea.val());
		this._textarea.animate({height:'80px'}, 200, $.proxy(this._showPostButton, this));
		this._handleOverflow();
	},
	_blurTextarea: function(){
		if(!this._textarea.val()){
			this._textarea.val(this._config.placeholder);
			this._hidePostButton();
			this._textarea.animate({height:'15px'}, 200, function(){});
		}
	},
	_showPostButton: function(){
		this._post_button.css('display', 'block');
		this._textarea.autogrow();
	},
	_hidePostButton: function(){
		this._post_button.css('display', 'none');
	},
	
	_handleOverflow: function(){
		if(this._textarea.val().length > this._config.max_length){
			this._textarea.val(this._textarea.val().substring(0, this._config.max_length));
		}
	},
	_postComment: function(){
		url = this._form.attr('action');
		data = this._form.serialize();
		
		$.ajax({
			type: "POST",
			url: url,
			data: data,
			success: $.proxy(this._handleSuccess, this),
			error: $.proxy(this._handleError, this),
			dataType: "json",
		});
	},
	_handleSuccess: function(data){
		if(!data.success){
			this._handleFailure(data);
			return;
		}
		var data_html = $(data.html).hide();
		data_html.insertBefore(this._form).fadeIn('slow');
		this._hidePostButton();
		this._textarea.animate({height:'15px'}, 200, function(){});
		this._textarea.val(this._config.placeholder);
	},
	_handleFailure: function(data){
		
	},

};
