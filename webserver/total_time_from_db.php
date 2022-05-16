<?php
include ("connect.php");

$set_row = "SET @row_number = 0;";

$total_sql_data = "SELECT table1.* FROM (SELECT A.id, A.Pi_room, A.Pi_time, A.Status, (TIME_TO_SEC(TIMEDIFF(B.Pi_time, A.Pi_time)) - 30) AS timedifference 
                   FROM (SELECT (@row_number:=@row_number + 1) AS num, `id`, `Pi_room`, `Pi_time`, `Status` FROM `db_table_room` WHERE `Status` = 'Activated' OR `Status` = 'Standby') A INNER JOIN (SELECT (@row_number:=@row_number + 1) AS num, `id`, `Pi_room`, `Pi_time`, `Status` FROM `db_table_room` WHERE `Status` = 'Activated' OR `Status` = 'Standby') B ON B.num = (A.num + (SELECT COUNT(`id`) FROM (SELECT `id`, `Pi_room`, `Pi_time`, `Status` FROM`db_table_room` WHERE `Status` = 'Activated' OR `Status` = 'Standby') as count_table) + 1)) table1 
                   LEFT OUTER JOIN `db_table_success_failures` table2 ON table1.Pi_time = table2.Pi_time_start WHERE table2.Status = 'Success'";
mysqli_query($conn, $set_row);
$total_result_data = mysqli_query($conn, $total_sql_data);
$total_number_of_rows = mysqli_num_rows($total_result_data);

//echo $total_number_of_rows;

if ($total_number_of_rows > 0) {
    // output data of each row
    while($row_data = mysqli_fetch_assoc($total_result_data)) {
    if ($row_data["Status"] == "Activated") {
      echo "Lightguidens started at: " . $row_data["Pi_time"] . "<br>" .
      "Lasted: " . $row_data["timedifference"] . " seconds" .  "<br><br>";
    }
    
    }

	//echo json_encode($data_points, JSON_NUMERIC_CHECK);

  } else {
    echo "0 data found";
  }
  
mysqli_close($conn);



?>
