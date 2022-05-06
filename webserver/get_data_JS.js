$(document).ready(function(){    
    loadstation();
});

function loadstation(){
    $("#live_data").load("data_from_db.php");
    setTimeout(loadstation, 2000);
    //setInterval(loadstation, 1000);
}


