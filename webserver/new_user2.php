<?php

session_start();
include ("connect.php");

function test_input($data) {
	
	$data = trim($data);
	$data = stripslashes($data);
	$data = htmlspecialchars($data);
	return $data;
}

if ($_SERVER["REQUEST_METHOD"]== "POST") {

$username = test_input($_POST["input_username"]);
$password = test_input($_POST["input_password"]);
$usertype = test_input($_POST["input_radio"]);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT id, username, user_password, usertype FROM db_table_login";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row

    foreach ($result as $row) {
        if(($row['username'] == $username) && ($row['user_password'] == $password)) 
                {
                    echo "<script language='javascript'>";
                    echo "alert('USER ALREADY EXIST')";
                    echo "</script>";
                    header( "refresh:0.5; url=register.php" ); 
                    die();
            }
        }    
    }

    $sql = "INSERT INTO db_table_login (id, username, user_password, usertype) VALUES (NULL, '$username', '$password', '$usertype')";
    if ($conn->query($sql) === TRUE) {
        echo "New account created successfully";
    } 
    else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
    $conn->close();

    } 
?>
<meta http-equiv="refresh" content="1; url=index.php">