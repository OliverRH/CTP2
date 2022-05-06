<?php

session_start();

include_once('connection.php');

function test_input($data) {
	
	$data = trim($data);
	$data = stripslashes($data);
	$data = htmlspecialchars($data);
	return $data;
}

if ($_SERVER["REQUEST_METHOD"]== "POST") {
	
	$username = test_input($_POST["username"]);
	$password = test_input($_POST["password"]);
	$stmt = $conn->prepare("SELECT * FROM db_table_login");
	$stmt->execute();
	$users = $stmt->fetchAll();
	
	foreach($users as $user) {
		
		if(($user['username'] == $username) && ($user['user_password'] == $password)) 
			{
				if(($user['usertype'] == "admin")){
					$_SESSION['usertype'] = "admin";
					header("Location: adminpage.php");
				}
				elseif(($user['usertype'] == "user"))
				{
					$_SESSION['usertype'] = "user";
					header("Location: userpage.php");
				}	
			}
	}
	echo "<script language='javascript'>";
			echo "alert('WRONG INFORMATION')";
			echo "</script>";
			header( "refresh:0.5; url=index.php" ); 
			die();
}

?>

<meta http-equiv="refresh" content="1; url=index.php">
