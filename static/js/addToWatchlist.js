$(document).ready(function() {
    if($("#add_to_watchlist").attr("data-alreadyin") == 1){
        $('#add_to_watchlist').hide();
    }

    $('#add_to_watchlist').click(function(){
        var movieid, userid;
        movieid = $("#add_to_watchlist").attr("data-movieid");
        userid = $("#add_to_watchlist").attr("data-userid");
        $.get('/movies/add_to_watchlist/', {m_id: movieid, u_id: userid}, function(data){
            $('#add_to_watchlist').hide();
        });
    });

});


