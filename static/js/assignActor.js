$(document).ready(function(){
    $(".assign").click(function(){
        var movieid = $(this).attr("data-movieid");
        var characterid = $(this).attr("data-characterid");
        var actorid = $("#s" + characterid).find(":selected").val();

        $.get('/movies/assign_actor/', {m_id: movieid, c_id: characterid, a_id: actorid}, function(data) {
            $("#d" + characterid).html(data);
        });
    });
});
