<?php
$servername = "localhost";
$dbname = "HAJTEK_Smart_Home_Care";
$dbusername = "root";
$dbpassword = "root";

// Create connection
$conn = mysqli_connect($servername, $dbusername, $dbpassword, $dbname);
// Check connection
if (!$conn) {
  die("Connection failed: " . mysqli_connect_error());
}
?>