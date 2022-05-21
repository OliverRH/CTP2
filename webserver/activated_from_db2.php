<?php
include ("connect.php");

$set_row1 = "SET @row_number1 = 0;";
$set_row2 = "SET @row_number2 = 0;";
$set_row3 = "SET @row_number3 = 0;";
$set_row4 = "SET @row_number4 = 0;";
$set_row5 = "SET @row_number5 = 0;";
$set_row6 = "SET @row_number6 = 0;";
$set_row7 = "SET @row_number7 = 0;";
$set_row8 = "SET @row_number8 = 0;";

mysqli_query($conn, $set_row1);
mysqli_query($conn, $set_row2);
mysqli_query($conn, $set_row3);
mysqli_query($conn, $set_row4);
mysqli_query($conn, $set_row5);
mysqli_query($conn, $set_row6);
mysqli_query($conn, $set_row7);
mysqli_query($conn, $set_row8);

$total_sql_data = "SELECT (total_difference2 - total_difference1) AS total_difference_total FROM
(SELECT *
FROM (SELECT(@row_number3:=@row_number3 + 1)AS num11, total_difference1 FROM (SELECT table1.* FROM (SELECT A.id, A.Pi_room,A.Pi_time, A.Status, (TIME_TO_SEC(TIMEDIFF(B.Pi_time, A.Pi_time))) AS total_difference1 FROM (SELECT (@row_number2:=@row_number2 + 1) AS num, `id`, `Pi_room`, `Pi_time`, `Status` FROM `db_table_room` WHERE `Pi_room` = 5 OR `Pi_room` = 1) A INNER JOIN (SELECT (@row_number1:=@row_number1 + 1) AS num, `id`, `Pi_room`, `Pi_time`, `Status` FROM `db_table_room` WHERE `Pi_room` = 5 OR `Pi_room` = 1) B ON B.num = (A.num + 1)) table1 LEFT OUTER JOIN `db_table_success_failures` table2 ON table1.Pi_time = table2.Pi_time_start WHERE table2.Status = 'Success') AS temp WHERE `Status` = 'running') table11

LEFT OUTER JOIN 

(SELECT (@row_number8:=@row_number8 + 1) AS num22, (timedifference1 - timedifference2) AS total_difference2 FROM (SELECT timedifference1, timedifference2 FROM (SELECT(@row_number7:=@row_number7 + 1) AS num1, table1.* FROM (SELECT A.id, A.Pi_room, A.Pi_time, A.Status, (TIME_TO_SEC(TIMEDIFF(B.Pi_time, A.Pi_time)) - 30) AS timedifference1 FROM (SELECT (@row_number6:=@row_number6 + 1) AS num, `id`, `Pi_room`, `Pi_time`, `Status` FROM `db_table_room` WHERE `Status` = 'Activated' OR `Status` = 'Standby') A INNER JOIN (SELECT (@row_number5:=@row_number5 + 1) AS num, `id`, `Pi_room`, `Pi_time`, `Status` FROM `db_table_room` WHERE `Status` = 'Activated' OR `Status` = 'Standby') B ON B.num = (A.num + 1)) table1 LEFT OUTER JOIN `db_table_success_failures` table2 ON table1.Pi_time = table2.Pi_time_start WHERE table2.Status = 'Success') table1 LEFT OUTER JOIN (SELECT (@row_number4:=@row_number4 + 1) AS num2, A.id, A.Pi_room, A.Pi_time, TIME_TO_SEC(TIMEDIFF(B.Pi_time, A.Pi_time)) AS timedifference2 FROM db_table_room A INNER JOIN db_table_room B ON B.id = (A.id + 1) WHERE A.Pi_room = 5) table2 ON table1.num1 = table2.num2) AS total) table22 
 
ON table11.num11 = table22.num22) AS total_diff";


$total_result_data = mysqli_query($conn, $total_sql_data);
$total_number_of_rows = mysqli_num_rows($total_result_data);

if ($total_number_of_rows > 0) {
    while($row_data = mysqli_fetch_assoc($total_result_data)) {
      echo "Time from the toilet took <br>" . $row_data["total_difference_total"] . " seconds" . "<br><br>";
    }

  } else {
    echo "";
  }
  
mysqli_close($conn);





?>
