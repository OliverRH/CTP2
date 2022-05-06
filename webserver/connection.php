<?php
session_start();


$conn = "";

try {
	$servername = "localhost";
	$dbname = "HAJTEK_Smart_Home_Care";
	$username = "root";
	$password = "root";

	$conn = new PDO(
		"mysql:host=$servername; dbname=HAJTEK_Smart_Home_Care",
		$username, $password
	);
	
$conn->setAttribute(PDO::ATTR_ERRMODE,
					PDO::ERRMODE_EXCEPTION);
}
catch(PDOException $e) {
	echo "Connection failed: " . $e->getMessage();
}

?>
