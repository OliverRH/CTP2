<?php
include ("connect.php");

$total_sql_data = "SELECT A.id, A.Pi_time, A.Pi_room, TIME_TO_SEC(TIMEDIFF(B.Pi_time, A.Pi_time)) AS timedifference FROM db_table_room A INNER JOIN db_table_room B ON B.id = (A.id + 1) ORDER BY A.id ASC";
$total_result_data = mysqli_query($conn, $total_sql_data);
$total_number_of_rows = mysqli_num_rows($total_result_data);

if ($total_number_of_rows > 0) {
    while($row_data = mysqli_fetch_assoc($total_result_data)) {
    echo "From room: " . $row_data["Pi_room"] . "<br>" .
    "Time: " . $row_data["Pi_time"] . "<br>" .
    "Timedifference: " . $row_data["timedifference"] . " seconds" . "<br><br>" ;
    }

  } else {
    echo "";
  }
  
mysqli_close($conn);





?>
