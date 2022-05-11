<?php
session_start();
?>

<!DOCTYPE html>
<html lang="en">
  
<head>
    <meta charset="UTF-8">  
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="login.css">
    <title>Register Page</title>
</head>
  
<body>


<div id="login" class="login-div"> 

<img src="hajtek_logo.png" class="logo">

<h1>Please pick a username and password.</h1>

<form action="new_user2.php" method="post">
  <fieldset>

    <p><input type="text" placeholder="Username" name="input_username" value="" style="text-transform: lowercase" required></p>
    

    <p><input type="password" placeholder="Password" name="input_password" value="" required></p>
    
    <p style="margin-bottom: 0px">Select if your are a admin or user:</p>
    <input class="radio-input" type="radio" id="admin_radio" name="input_radio" value="admin" required>
    <label class="radio-label" for="admin_radio">Admin</label>
    <input class="radio-input" type="radio" id="user_radio" name="input_radio" value="user" required>
    <label class="radio-label" for="user_radio">User</label><br>  
   
    <p style="margin-top: 10px"><input class="button" type="submit" name="login" value="Sign In"></p>

  </fieldset>

</form>



</div>  
</body>
  
</html>