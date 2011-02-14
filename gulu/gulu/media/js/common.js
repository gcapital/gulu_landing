$(document).ready(function(){
	// jump to specific anchor if url match the regex rule 
	var path =  location.pathname;
	var conti = true;
	

	for( var i in regexs = [
		/^\/[a-zA-Z\-]+\/reviews\/$/,
		/^\/[a-zA-Z\-]+\/photos\/$/,
	]){
		if(path.match(regexs[i]))
		{
			$(window).scrollTop(190);
			conti=false;
			break;
		}	
	}
	
	for( var i in regexs = [
		/^\/[a-zA-Z\-]+\/reviews\/[\w0-9]+\/$/,
		/^\/[a-zA-Z\-]+\/photos\/[\w0-9]+\/$/,
	]){
		if(path.match(regexs[i]))
		{
			$(window).scrollTop(420);
			conti=false;
			break;
		}
	}
});
