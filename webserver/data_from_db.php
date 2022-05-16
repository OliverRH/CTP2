<?php
include ("connect.php");

$total_sql_data = "SELECT COUNT(`Pi_room`) AS entries, DATE_FORMAT(`Pi_time`, '%d/%m/%Y') as date FROM `db_table_room` WHERE `Pi_room` = 5 GROUP BY DATE_FORMAT(`Pi_time`, '%d/%m/%Y') LIMIT 0 , 31";
$total_result_data = mysqli_query($conn, $total_sql_data);
$total_number_of_rows = mysqli_num_rows($total_result_data);

if ($total_number_of_rows > 0) {
    // output data of each row
    while($row_data = mysqli_fetch_assoc($total_result_data)) {
    echo "Date: " . $row_data["date"] . "<br>" .
    "Bathroom trips: " . $row_data["entries"] . "<br><br>" ;
    
    }

  } else {
    echo "0 data found";
  }
  
mysqli_close($conn);





?>
