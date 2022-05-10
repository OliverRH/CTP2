<?php
session_start();
ob_start();
if (isset($_SESSION['usertype']) != "admin") die ('Du skal være logget ind som user for at se denne side!') 
?>

<?php
include ("connect.php");

/*
$total_sql_data = "SELECT * FROM `db_table_room`";
//$sql_data = "SELECT Pi_room, Pi_time FROM db_table_room";
$total_result_data = mysqli_query($conn, $total_sql_data);

$total_number_of_rows = mysqli_num_rows($total_result_data);

echo "!!" . $total_number_of_rows . "!!";

$sql_start_date = "SELECT `id` FROM `db_table_room` WHERE id=(SELECT min(id) FROM `db_table_room`)";
$sql_end_date = "SELECT `id` FROM `db_table_room` WHERE id=(SELECT max(id) FROM `db_table_room`)";

echo "START: " . $sql_start_date;
echo "END: " . $sql_start_date;

for ($i=0; $i < ; $i++) { 
	# code...
}

if ($total_result_data > 0) {
    // output data of each row
    while($row_data = mysqli_fetch_assoc($result_data)) {
		
		$jsonArrayItem['label'] = $row_data["Pi_time"];
		array_push($jsonArray, $jsonArrayItem);	
    }
  } else {
    echo "0 data found";
  }
*/



//$sql_data = "SELECT * FROM `db_table_room` WHERE `Pi_time` >= CAST('2022-05-06' AS DATE) AND `Pi_time` <= CAST('2022-05-28' AS DATE)";
//$sql_data = "SELECT Pi_room, Pi_time FROM db_table_room";
//$result_data = mysqli_query($conn, $sql_data);

//$sql_start_date = "SELECT `id` FROM `db_table_room` WHERE id=(SELECT min(id) FROM `db_table_room`)";
//$result_data_start_date = mysqli_fetch_assoc(mysqli_query($conn, $sql_start_date))['id'];
//sql_end_date = "SELECT `id` FROM `db_table_room` WHERE id=(SELECT max(id) FROM `db_table_room`)";
//result_data_end_date = mysqli_fetch_assoc(mysqli_query($conn, $sql_end_date))['id'];
//
//cho "START: " . $result_data_start_date;
//cho "END: " . $result_data_end_date

$total_sql_data = "SELECT COUNT(`id`) AS entries, DATE_FORMAT(`Pi_time`, '%d/%m/%Y') as date FROM `db_table_room` WHERE `Pi_time` GROUP BY DATE_FORMAT(`Pi_time`, '%d/%m/%Y') LIMIT 0 , 31";
$total_result_data = mysqli_query($conn, $total_sql_data);
$total_number_of_rows = mysqli_num_rows($total_result_data);

$data_points = array();

//echo $total_number_of_rows;

if ($total_number_of_rows > 0) {
    // output data of each row
    while($row_data = mysqli_fetch_assoc($total_result_data)) {
		$jsonArrayItem = array();
		$jsonArrayItem['y'] = $row_data["entries"];
		$jsonArrayItem['label'] = $row_data["date"];
		array_push($data_points, $jsonArrayItem);	
    }

	//echo json_encode($data_points, JSON_NUMERIC_CHECK);

  } else {
    echo "0 data found";
  }
  



$total_sql_data2 = "SELECT A.id, A.Pi_room, A.Pi_time, TIME_TO_SEC(TIMEDIFF(B.Pi_time, A.Pi_time)) AS timedifference FROM db_table_room A INNER JOIN db_table_room B ON B.id = (A.id + 1) WHERE A.Pi_room = 4 or A.Pi_room = 5 ";
$total_result_data2 = mysqli_query($conn, $total_sql_data2);
$total_number_of_rows2 = mysqli_num_rows($total_result_data2);

$data_points2 = array();

//echo $total_number_of_rows;

if ($total_number_of_rows2 > 0) {
    // output data of each row
    while($row_data2 = mysqli_fetch_assoc($total_result_data2)) {
		if ($row_data2["Pi_room"] == 5) {
			$jsonArrayItem2 = array();
			$jsonArrayItem2['y'] = $row_data2["timedifference"];
			$jsonArrayItem2['label'] = $row_data2["Pi_time"];
			array_push($data_points2, $jsonArrayItem2);	
		  }
    }

	//echo json_encode($data_points, JSON_NUMERIC_CHECK);

  } else {
    echo "0 data found";
  }
  
mysqli_close($conn)








//echo json_encode($jsonArray);

/*
if ($total_number_of_rows > 0) {
	for ($i = $total_number_of_rows; $i > 0; $i--) { 
		$sql_start_date = "SELECT `id` FROM `db_table_room` WHERE id=(SELECT min(id) FROM `db_table_room`)";
		$result_data_start_date = mysqli_fetch_assoc(mysqli_query($conn, $sql_start_date))['id'];
		while()
		echo "Din mor";
	}
  }
  
mysqli_close($conn);
*/




//$jsonArray = array();
//$number_of_rows = mysqli_num_rows($result_data);
////echo $number_of_rows;
//
//$jsonArrayItem = array();
//$jsonArrayItem['y'] = $number_of_rows;
//
//
//if ($number_of_rows > 0) {
//    // output data of each row
//    while($row_data = mysqli_fetch_assoc($result_data)) {
//		
//		$jsonArrayItem['label'] = $row_data["Pi_time"];
//		array_push($jsonArray, $jsonArrayItem);	
//    }
//  } else {
//    echo "0 data found";
//  }
//  
//mysqli_close($conn);
//
////header('Content-type: application/json');
//
//
//echo json_encode($jsonArray);




?>



<!DOCTYPE html>
<html lang="en">
  
<head>
    <meta charset="UTF-8">  
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
		
		
	<script>
		
	window.onload = function () {
	var chart = new CanvasJS.Chart("chartContainer", {
		animationEnabled: true,
		backgroundColor: "#f4f4f4",
		theme: "light2", // "light1", "light2", "dark1", "dark2"
		title: {
			text: "Number of toilet visits per day",
			fontSize: 20,
		},
		axisY: {
			labelFontSize: 12,
			titleFontSize: 20,
			interval: 10,
			interlacedColor: "#EEEEEE",
      		tickLength: 1,
		},
		axisX: {
			labelFontSize: 12,
			titleFontSize: 20,
		},
		data: [{
			type: "column",
			dataPoints: <?php echo json_encode($data_points, JSON_NUMERIC_CHECK); ?>
		}]
	});
	chart.render();	
	
	var chart = new CanvasJS.Chart("chartContainer2", {
		animationEnabled: true,
		backgroundColor: "#f4f4f4",
		theme: "light2", // "light1", "light2", "dark1", "dark2"
		title: {
			text: "Time on the toilet in seconds",
			fontSize: 20,
		},
		axisY: {
			labelFontSize: 12,
			titleFontSize: 20,
			interval: 100,
			interlacedColor: "#EEEEEE",
      		tickLength: 1,
		},
		axisX: {
			labelFontSize: 12,
			titleFontSize: 20,
		},
		data: [{
			type: "column",
			dataPoints: <?php echo json_encode($data_points2, JSON_NUMERIC_CHECK); ?>
		}]
	});
	chart.render();	
	}
	
	
	</script>


	







	
    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
    <script src="get_timediff_JS.js"></script>
    <link rel="stylesheet" href="userpage_CSS.css">
    <title>LIVE - Dashboard</title>
</head>
  
<body>



<div>
	<div id="chartContainer"></div>
	<div id="chartContainer2"></div>
	<script src="https://canvasjs.com/assets/script/canvasjs.min.js"></script>

	<div id="div_data" ><p id="data_head">Bathroom trips:</p></div>
	<div id="div_live_data">
		<div id="live_data"></div>
	</div>
	<div id="div_data" style="left: 230px;" ><p id="data_head">Time between rooms:</p></div>
	<div id="div_live_timediff">
		<div id="live_timediff"></div>
	</div>
	<div id="div_data" style="left: 495px;" ><p id="data_head">Time on the toilet:</p></div>
	<div id="div_live_time_on_toilet">
		<div id="live_time_on_toilet"></div>
	</div>

	<div id="div_data" style="left: 495px; top: 85%" ><p id="data_head">Success rate:</p></div>
	<div id="div_live_made_it">
		<div id="live_made_it"></div>
	</div>

	<div class="btn-group">
		
		<a href="logout.php" class="btn-group_button">Log ud!</a>
		
		<form action="delete_data.php" method="post">
    		<input class="btn-group_button" type="submit" name="login" value="Delete all data in database">
		</form>
		
	</div>

<div id="admin_panel">
	<form action="" method="post">
		<div class="inline">
			<select name="Zigbee_sub">
				<?php 
					include ("connect.php");
					$sql = mysqli_query($conn, "SELECT * FROM db_table_zigbee");
					while ($row = $sql->fetch_assoc()){
					echo "<option value=" . $row['Zigbee_name'] . ">" . $row['Zigbee_addr'] . "</option>";
					}
				?>
			</select>
				<select name="Zigbee_pub">
				<?php 
					include ("connect.php");
					$sql = mysqli_query($conn, "SELECT * FROM db_table_zigbee");
					while ($row = $sql->fetch_assoc()){
					echo "<option value=" . $row['Zigbee_name'] . ">" . $row['Zigbee_name'] . "</option>";
					}
				?>
			</select>
			<input type="submit" name="submit" value = "Choose this combination">
		</div>
	</form>
</div>
		

<?php
    if(isset($_POST['submit'])){
		$selected1 = $_POST['Zigbee_sub'];
		$selected2 = $_POST['Zigbee_pub'];
        echo 'You have chosen: ' . $selected1 . " --> " . $selected2;
    };



?>
	
</div>





</div>

</body>
  
</html>

