<?php
include ("connect.php");

$total_sql_data = "SELECT Status, COUNT( Status ) AS thecount, FORMAT(((COUNT( Status ) / ( SELECT MAX(id) FROM `db_table_success_failures`)) * 100 ),2) AS percentage FROM `db_table_success_failures` GROUP BY Status ORDER BY thecount DESC LIMIT 50";
$total_result_data = mysqli_query($conn, $total_sql_data);
$total_number_of_rows = mysqli_num_rows($total_result_data);

if ($total_number_of_rows > 0) {
    while($row_data = mysqli_fetch_assoc($total_result_data)) {
        echo $row_data["Status"] . ": " . $row_data["percentage"] . "%". "<br>" ;
    }

  } else {
    echo "";
  }
  
mysqli_close($conn);





?>
