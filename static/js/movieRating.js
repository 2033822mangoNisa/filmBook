$(document).ready(function(){
    // more complex jRating call
    $(".star_rating").jRating({
        canRateAgain: true,
        step: true,
        length : 10,
        rateMax : 10,
        nbRates : 100,
        showRateInfo : false,

        onClick : function(element,rate) {
            var movieid, userid;
            movieid = $(".star_rating").attr("data-movieid");
            userid = $(".star_rating").attr("data-userid");
            $.get('/movies/rate/', {m_id: movieid, u_id: userid, r: rate}, function(data){
                $('#rating').html(data);
            });

        }
    });


});
