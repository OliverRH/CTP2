// Turn on the light in a room (click)
$(document).ready(function() {
    $(".room").click(function(event) {
       event.preventDefault(); 
       $(".simple-bulb").css("visibility", "hidden");
       $(this).children(".simple-bulb").css("visibility", "visible");
     });
 });