<?php
    function OpenCon()
    {
        $dbhost = "localhost";
        $dbuser = "root";
        $dbpass = "admin"; //or whatever you choose when you installed it
        $db = "hello";
        $conn = new mysqli($dbhost, $dbuser, $dbpass,$db)
            or die("Connect failed: %s\n". $conn -> error);
        return $conn;
    }
    function CloseCon($conn)
    {
    $conn -> close();
    }
?>