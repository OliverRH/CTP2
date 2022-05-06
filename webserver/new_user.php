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
    $usertype = "admin"; //test_input($_POST["usertype"]);
	$stmt = $conn->prepare("SELECT * FROM db_table_login");
	$stmt -> execute();
	$users = $stmt->fetchAll();
	
	foreach($users as $user) {
        
		if(($user['username'] == $username) && ($user['password'] == $password)) 
			{
                echo "<script language='javascript'>";
			    echo "alert('USER ALREADY EXIST')";
			    echo "</script>";
			    header( "refresh:0.5; url=index.php" ); 
			    die();
			}
        else {
            break;

            /*
            if (!$conn) {
            die("Connection failed: " . mysqli_connect_error());
            }

            $sql = "INSERT INTO db_table_login ('id', 'username', 'password', 'usertype') VALUES (NULL, $username, $password, $usertype)";
            
            if (mysqli_query($conn, $sql)) {
            echo "New record created successfully";
            } else {
            echo "Error: " . $sql . "<br>" . mysqli_error($conn);
            }

            mysqli_close($conn);
            */




            /*
            $sql = "INSERT INTO db_table_login ('id', 'username', 'password', 'usertype') VALUES (NULL, $username, $password, $usertype)";
            echo $sql;
            if ($conn->query($sql) == TRUE) {
            echo "New record created successfully";
            } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
            }
            $conn->close();
            */
        }
        break;
    }
    $sql = $sql = "INSERT INTO db_table_login (id, username, user_password, usertype) VALUES (NULL, $username, $password, 'admin')";
            echo $sql;
            if ($conn->query($sql) == TRUE) {
            echo "New record created successfully";
            } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
            }
            $conn->close();
}
    

?>
<meta http-equiv="refresh" content="1; url=index.php">

