/**
 * Gulu Photos AJAX upload widget
 *
 * Creates an AJAX upload widget specific to Gulu.  Requires Andrew Valum's
 * file-uploader <http://github.com/valums/file-uploader>.  
 *
 * @author Ben Homnick <bhomnick@gmail.com>
 */
 
var Photos = Photos || {};
 
/**
 * AJAX Uploader
 * Creates an AJAX upload widget specific to Gulu.  Requires Andrew Valum's
 * file-uploader <http://github.com/valums/file-uploader>.  
 */
Photos.AjaxUploader = function(config){
	this._config = {
		button: null,				// jQuery selector of upload button
		imagespec: 'image185x185',	// Image spec of preview to return
		errors:	null,				// jQuery selector of container to display errors
		preview: null,				// jQuery selector of img tag to display preview
		progress: null,				// jQuery selector of progress percent container
		input: null,				// jQuery selector of input to save temp photo id
		url_input: null,			// jQuery selector of input to save temp photo url
	};
	$.extend(this._config, config);
	
	var uploader = new qq.FileUploaderBasic({
		button: this._config.button[0],
		action: '/photos/ajax/upload_photo',
		onProgress: $.proxy(this._updateProgress, this),
		onSubmit: $.proxy(this._startUpload, this),
		onComplete: $.proxy(this._finishUpload, this),
		debug: true,
		params: {
			'spec': this._config.imagespec,
		},
	});

	// Restore initial data
	default_data = this._config.input.val();
	if(default_data != null && default_data != ""){
		var img = $('<img src="'+this._config.url_input.val()+'">');
		this._config.preview.append(img.hide().fadeIn(2000));
	}

};

Photos.AjaxUploader.prototype = {
	_startUpload: function(id, file){
		this._config.preview.fadeOut(600);
		this._config.input.val("");
		var img = $('<img src="/media/images/icon_loading.gif">');
		this._config.preview.html(img);
		this._config.preview.fadeIn(100);
	},
	_updateProgress: function(id, file, loaded, total){
		//this._config.progress.text(loaded/total*100);
	},
	_finishUpload: function(id, file, response){
		if(response.status == 1){
			var img = $('<img src="'+response.url+'">');
			this._config.preview.html(img);
			this._config.preview.fadeIn(1000);
			this._config.input.val(response.id);
			this._config.url_input.val(response.url);
		}
		else{
			this._handleError(response.message);
		}
	},
	_handleError: function(message){
		this._config.error.text(message);
	},
	
};
