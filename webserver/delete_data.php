<?php

session_start();

include_once('connection.php');

$delete_table_sql = "TRUNCATE `db_table_room`";

if ($conn->query($delete_table_sql) ==  TRUE) {
    echo "Date deleted successfully";
  } else {
    echo "Error deleting data: " . $conn->error;
  }
  
mysqli_close($conn)

?>

<meta http-equiv="refresh" content="1; url=userpage.php">
