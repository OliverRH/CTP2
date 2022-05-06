<?php
session_start();
ob_start();
if (isset($_SESSION['usertype']) != "admin") die ('Du skal være logget ind som admin for at se denne side!') 
?>

<!DOCTYPE html>
<html lang="en">
  
<head>
    <meta charset="UTF-8">  
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="login.css">
    <title>Login Page</title>
</head>
  
<body>

<h2>Hello Admin </h2>

<?php       
    echo 'Du er logget ind som: ' . $_SESSION['usertype'];
?> 


<a href="logout.php">Log ud!</a>

</body>
  
</html>