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

$total_sql_data = "SELECT A.id, A.Pi_room, A.Pi_time, TIME_TO_SEC(TIMEDIFF(B.Pi_time, A.Pi_time)) AS timedifference FROM db_table_room A INNER JOIN db_table_room B ON B.id = (A.id + 1) WHERE A.Pi_room = 5";
$total_result_data = mysqli_query($conn, $total_sql_data);
$total_number_of_rows = mysqli_num_rows($total_result_data);

$data_points = array();

//echo $total_number_of_rows;

if ($total_number_of_rows > 0) {
    // output data of each row
    while($row_data = mysqli_fetch_assoc($total_result_data)) {
        echo "Start time: " . $row_data["Pi_time"] . "<br>" . "Time on the toilet: " . $row_data["timedifference"] . " seconds" . "<br><br>" ;
        
    }

	//echo json_encode($data_points, JSON_NUMERIC_CHECK);

  } else {
    echo "0 data found";
  }
  
mysqli_close($conn);





?>
