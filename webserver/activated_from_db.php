<?php
include ("connect.php");

/*
$sql_data = "SELECT Pi_room, Pi_time FROM db_table_room";
$result_data = mysqli_query($conn, $sql_data);
if (mysqli_num_rows($result_data) > 0) {
    // output data of each row
    while($row_data = mysqli_fetch_assoc($result_data)) {
      echo "Room: " . $row_data["Pi_room"] . "<br>" .
      "Time: " . $row_data["Pi_time"] . "<br>" ;
    }
  } else {
    echo "0 data found";
  }

  
  mysqli_close($conn);



$total_sql_data = "SELECT COUNT(`id`) AS entries, DATE_FORMAT(`Pi_time`, '%d/%m/%Y') as date FROM `db_table_room` WHERE `Pi_time` GROUP BY DATE_FORMAT(`Pi_time`, '%d/%m/%Y') LIMIT 0 , 31";
$total_result_data = mysqli_query($conn, $total_sql_data);
$total_number_of_rows = mysqli_num_rows($total_result_data);

if ($total_number_of_rows > 0) {
    // output data of each row
    while($row_data = mysqli_fetch_assoc($total_result_data)) {
      echo "Date: " . $row_data["date"] . "<br>" .
      "Number of visits: " . $row_data["entries"] . "<br><br>" ;
    }
  } else {
    echo "0 data found";
  }
  
mysqli_close($conn);

*/

$set_row = "SET @row_number = 0;";

$total_sql_data = "SELECT table1.* FROM (SELECT A.id, A.Pi_room, A.Pi_time, A.Status, (TIME_TO_SEC(TIMEDIFF(B.Pi_time, A.Pi_time))) AS timedifference FROM (SELECT (@row_number:=@row_number + 1) AS num, `id`, `Pi_room`, `Pi_time`, `Status` FROM `db_table_room` WHERE `Pi_room` = 5 OR `Pi_room` = 1) A INNER JOIN (SELECT (@row_number:=@row_number + 1) AS num, `id`, `Pi_room`, `Pi_time`, `Status` FROM `db_table_room` WHERE `Pi_room` = 5 OR `Pi_room` = 1) B ON B.num = (A.num + (SELECT COUNT(`id`) FROM (SELECT `id`, `Pi_room`, `Pi_time`, `Status` FROM `db_table_room` WHERE `Pi_room` = 5 OR `Pi_room` = 1) as count_table) + 1)) table1 LEFT OUTER JOIN `db_table_success_failures` table2 ON table1.Pi_time = table2.Pi_time_start WHERE table2.Status = 'Success'";
mysqli_query($conn, $set_row);
$total_result_data = mysqli_query($conn, $total_sql_data);
$total_number_of_rows = mysqli_num_rows($total_result_data);

//echo $total_number_of_rows;

if ($total_number_of_rows > 0) {
    // output data of each row
    while($row_data = mysqli_fetch_assoc($total_result_data)) {
    if ($row_data["Pi_room"] == 1 && $row_data["Status"] == "running") {
      echo "Time to the toilet from room " . $row_data["Pi_room"] . "<br>" . "took " . $row_data["timedifference"] . " seconds" . "<br><br>";
    }
    
    }

	//echo json_encode($data_points, JSON_NUMERIC_CHECK);

  } else {
    echo "0 data found";
  }
  
mysqli_close($conn);





?>
