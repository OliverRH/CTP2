$(document).ready(function(){    
    loadstation();
});

function loadstation(){
    $("#live_data").load("data_from_db.php");
    $("#live_timediff").load("timediff_from_db.php");
    $("#live_time_on_toilet").load("how_long_on_toilet.php");
    $("#live_made_it").load("made_it.php");
    $("#activated_data").load("activated_from_db.php");
    $("#activated_data2").load("activated_from_db2.php");
    $("#total_time_data").load("total_time_from_db.php");
    setTimeout(loadstation, 2000);
    //setInterval(loadstation, 1000);
}


