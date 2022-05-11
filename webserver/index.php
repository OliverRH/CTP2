<?php
session_start();
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


<div id="login" class="login-div"> 

<img src="hajtek_logo.png" class="logo">

<h1><strong>Welcome.</strong> Please login.</h1>

<form action="validate.php" method="post">
  <fieldset>

    <p><input type="text" placeholder="Username" name="username" value="" style="text-transform: lowercase" required></p>

    <p><input type="password" placeholder="Password" name="password" value=""required></p>

    <p><input class="button" type="submit"
                     name="login" value="Sign In"></p>
    <p><a href="register.php">Not a user? Register here!</a></p>
  </fieldset>

</form>



</div>  
</body>
  
</html>