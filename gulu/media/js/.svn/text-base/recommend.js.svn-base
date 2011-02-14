/* Gulu Recommend module JS */
Recommend = {};
Recommend.ItemPerUser = 20;
Recommend.PendingSave = 0;

Recommend.Init = function() {
	
	$('.restaurant_tab').click(function(){
		$(this).addClass('top');
		$('.dish_tab').removeClass('top');
		$('#restaurant_ranking').removeClass('display_none');
		$('#dish_ranking').addClass('display_none')
	});
	
	$('.dish_tab').click(function(){
		$(this).addClass('top');
		$('.restaurant_tab').removeClass('top');
		$('#dish_ranking').removeClass('display_none');
		$('#restaurant_ranking').addClass('display_none')
	});
	
    jQuery ('#restaurant_ranking').sortable({
        cursor: 'move',
        update: function(event,ui){
            var ranking = $('#restaurant_ranking').sortable('toArray');
            var score = Recommend.ItemPerUser;
            ui.item.find('.saving').fadeIn('slow');
            for (var i=0 ;i<ranking.length ;i++)
                Recommend.Update ('restaurant', ranking[i], score--);
            ui.item.find('.saving').fadeOut('slow');
        }
    });
    
    jQuery ('#dish_ranking').sortable({
        cursor: 'move',
        update: function(event,ui){
            var ranking = $('#dish_ranking').sortable('toArray');
            var score = Recommend.ItemPerUser;
            ui.item.find('.saving').fadeIn('slow');
            for (var i=0 ;i<ranking.length ;i++)
                Recommend.Update ('dish', ranking[i], score--);
            ui.item.find('.saving').fadeOut('slow');
        }
    });
    
    $('.list li').hover(function(){
    	$(this).addClass('hover');
    },function(){
    	$(this).removeClass('hover');
    });
}

Recommend.Update = function(_type, _id, _score) {
    Recommend.PendingSave++;
    $.ajax({
        url: "/recommend/ajax/update",
        type: 'POST',
        data: ({
            type: _type,
            id: _id,
            score: _score
        }),
        success: function (){
            Recommend.PendingSave--;
            if (_type=="restaurant")
                $('#r_'+_id).text(21-parseInt(_score));
            else
                $('#d_'+_id).text(21-parseInt(_score));
        } 
    });
}

