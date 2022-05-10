$(document).ready(function(){    
    loadstation();
});

function loadstation(){
    $("#live_timediff").load("timediff_from_db.php");
    setTimeout(loadstation, 2000);
    //setInterval(loadstation, 1000);
}


