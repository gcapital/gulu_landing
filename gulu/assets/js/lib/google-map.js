var GMap = {
	'GetMapByLatlng' : function(latlng, id, zoom, type, flag) {
	    zoom = zoom || 13;
	    type = type || google.maps.MapTypeId.ROADMAP;
	    flag = flag || true;
	
	    var myOptions = {
	        'zoom': zoom,
	        'center': latlng,
	        'mapTypeId': type,
	        'scrollwheel': false
	    };
	    var map = new google.maps.Map(document.getElementById(id), myOptions);
	    if(flag)
	    {
	        var marker = new google.maps.Marker({
	          map: map,
	          position: latlng
	        });
	    }
	    return map;
	},

	'GetMapByAddress' : function(address, id, zoom, type, flag) {
	    var geocoder = new google.maps.Geocoder();
	    geocoder.geocode({'address':address},function(results,status){
	        if (status == google.maps.GeocoderStatus.OK) {
	
	            latlng = results[0].geometry.location;
	            var map = new GMap.GetMapByLatlng(latlng,id, zoom, type, flag);
	
	        } else {
	          alert("Geocode was not successful for the following reason: " + status);
	        }
	    });
	},
}