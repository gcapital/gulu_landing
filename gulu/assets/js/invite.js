/* Gulu Event module JS */
Invite = {}


Invite.InviteChoice = {}
	
Invite.InviteChoice._config = {
	'invite_choice_container': null,	// Selector of container to display available user choices
	'sms_invite_container': null,		// Container for displaying number of SMS invites used
	'search_form_input': null,			// Selector of user search filter input (textbox)
	'save_form': null,					// Selector of the save form
	'save_form_submit': null,			// Form save button selector
	'selected_invites_input': null,		// Hidden input selector to hold user invite checkbox data
	'other_sms_input': null				// Input field for other SMS invites	
};	

Invite.InviteChoice._invite_ids = [];
Invite.InviteChoice._sms_invite_count = 0;
Invite.InviteChoice._sms_other_count = 0;

// Invite choice picker initialization function
Invite.InviteChoice.init = function(_user_config) {
	// extend the default config with the user's config
	$.extend(Invite.InviteChoice._config, _user_config);
	
	// if the form was already submitted and had errors, make sure
	// to use the last state as default
	default_data = $(Invite.InviteChoice._config['selected_invites_input']).val();
	if(default_data != null && default_data != ""){
		Invite.InviteChoice._invite_ids = default_data.split(",");
		for(i in Invite.InviteChoice._invite_ids){
			invite = Invite.InviteChoice._invite_ids[i].split("_");
			if(invite[0] == 'sms'){
				Invite.InviteChoice._sms_invite_count++;
			}
		}
	}
	
	// populate the selector
	Invite.InviteChoice.getInviteChoices();
	Invite.InviteChoice.updateUI();
	
	// mask the other SMS input
	$(Invite.InviteChoice._config['other_sms_input']).numeric({allow:"., +-"});
	
	// get default data for other SMS
	default_other_sms = $(Invite.InviteChoice._config['other_sms_input']).val();
	if(default_other_sms != null && default_other_sms != ""){
		Invite.InviteChoice.updateOtherSMS(default_other_sms);
	}
	
	// bind the necessary events
	$(Invite.InviteChoice._config['invite_choice_container'] + " input:checkbox").live('click', function() {
		Invite.InviteChoice.clickChoice($(this));
	});
	$(Invite.InviteChoice._config['save_form_submit']).live('click', function() {
		Invite.InviteChoice.submitForm();
	});
	$(Invite.InviteChoice._config['search_form_input']).keyup(function() {
		Invite.InviteChoice.getInviteChoices($(this).val());
	});	
	$(Invite.InviteChoice._config['other_sms_input']).keyup(function() {
		Invite.InviteChoice.updateOtherSMS($(this).val());
	});
	
}

// Do an ajax query to get available invite choices, optionally specifying a search term
Invite.InviteChoice.getInviteChoices = function(query) {
	url = '/invite/ajax/get-invite-choices'
	$.getJSON(url, {'q': query}, Invite.InviteChoice.displayInviteChoices);
}

// Display the invite choices returned from getInviteChoices()		
Invite.InviteChoice.displayInviteChoices = function(data) {
	$(Invite.InviteChoice._config['invite_choice_container']).html('');
		
	for(i in data) {
		
		id = data[i]['type'] + '_' + data[i]['id'];
		sms_id = 'sms_' + id;
		email_id = 'email_' + id;
		
		// create the element
		src = '';
		src += '<div class="invite_choice">';
			src += '<div class="invite_choice_name">';
				src += data[i]['name'];
			src += '</div>';
			src += '<div class="invite_choice_img"><img src="' + data[i]['pic'] + '"></div>';
			src += '<div class="invite_choice_checkboxes">';
			src += '<p>';
				src += '<label for="' + email_id + '">Email</label>';
				src += '<input type="checkbox" name="name_' + email_id + '" id="'+ email_id + '" />';
			src += '</p>';
			src += '<p>';
				src += '<label for="' + sms_id + '">SMS</label>';
				src += '<input type="checkbox" name="name_' + sms_id + '" id="'+ sms_id + '" />';
			src += '</p>';
			src += '</div>';
		src += '</div>';
	
		// append it to the view
		$(Invite.InviteChoice._config['invite_choice_container']).append(src);
	}
	
	// check any boxes that were checked before
	for(i in Invite.InviteChoice._invite_ids){
		$('#' + Invite.InviteChoice._invite_ids[i]).attr('checked', true);
	}
}

// Called when an SMS or Email checkbox is clicked
Invite.InviteChoice.clickChoice = function(element) {
	element_id = element.attr('id');
	element_info = element_id.split('_');
	
	/*
	element_info:
	[0] = <{email|sms}>
	[1] = <{follower|contact}>
	[2] = <id>
	*/
	
	if(element.is(':checked')){
		Invite.InviteChoice._invite_ids.push(element_id);
		if(element_info[0] == 'sms'){
			Invite.InviteChoice._sms_invite_count += 1;
		}
	}
	else{
		Invite.InviteChoice._invite_ids.splice($.inArray(element_id, Invite.InviteChoice._invite_ids), 1);
		if(element_info[0] == 'sms'){
			Invite.InviteChoice._sms_invite_count -= 1;
		}
	}
	
	Invite.InviteChoice.updateUI();
}

// count the number of other SMS
Invite.InviteChoice.updateOtherSMS = function(sms_string) {
	var count = 0;
	sms = sms_string.split(",");
	for(i in sms){
		if(jQuery.trim(sms[i]) != "" && jQuery.trim(sms[i]) != null){
			count++;
		}
	}
	Invite.InviteChoice._sms_other_count = count;
	Invite.InviteChoice.updateUI();
}

// Updates various UI elements (# sms invited, total users, etc)
Invite.InviteChoice.updateUI = function() {
	var total_sms = Invite.InviteChoice._sms_invite_count + Invite.InviteChoice._sms_other_count;
	$(Invite.InviteChoice._config['sms_invite_container']).html(total_sms);
}


Invite.InviteChoice.submitForm = function() {
	$(Invite.InviteChoice._config['selected_invites_input']).val(Invite.InviteChoice._invite_ids.join(','));
	$(Invite.InviteChoice._config['save_form']).submit();
}
