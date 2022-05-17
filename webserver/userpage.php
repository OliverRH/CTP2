<?php
session_start();
ob_start();
if (isset($_SESSION['usertype']) != "user") die ('You need to be logged as a user to view this page!') 
?>

<?php
include ("connect.php");

$total_sql_data = "SELECT COUNT(`Pi_room`) AS entries, DATE_FORMAT(`Pi_time`, '%d/%m/%Y') as date FROM `db_table_room` WHERE `Pi_room` = 5 GROUP BY DATE_FORMAT(`Pi_time`, '%d/%m/%Y') LIMIT 0 , 31";
$total_result_data = mysqli_query($conn, $total_sql_data);
$total_number_of_rows = mysqli_num_rows($total_result_data);

$data_points = array();

if ($total_number_of_rows > 0) {

    while($row_data = mysqli_fetch_assoc($total_result_data)) {
		$jsonArrayItem = array();
		$jsonArrayItem['y'] = $row_data["entries"];
		$jsonArrayItem['label'] = $row_data["date"];
		array_push($data_points, $jsonArrayItem);	
    }

  } else {
    
  }


$total_sql_data2 = "SELECT A.id, A.Pi_room, A.Pi_time, TIME_TO_SEC(TIMEDIFF(B.Pi_time, A.Pi_time)) AS timedifference FROM db_table_room A INNER JOIN db_table_room B ON B.id = (A.id + 1) WHERE A.Pi_room = 4 or A.Pi_room = 5 ";
$total_result_data2 = mysqli_query($conn, $total_sql_data2);
$total_number_of_rows2 = mysqli_num_rows($total_result_data2);

$data_points2 = array();



if ($total_number_of_rows2 > 0) {

    while($row_data2 = mysqli_fetch_assoc($total_result_data2)) {
		if ($row_data2["Pi_room"] == 5) {
			$jsonArrayItem2 = array();
			$jsonArrayItem2['y'] = $row_data2["timedifference"];
			$jsonArrayItem2['label'] = $row_data2["Pi_time"];
			array_push($data_points2, $jsonArrayItem2);	
		  }
    }


  } else {
    
  }
  
mysqli_close($conn)


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
			text: "Number of bathroom trips per day",
			fontSize: 20,
		},
		axisY: {
			labelFontSize: 12,
			titleFontSize: 20,
			interval: 1,
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

	<div id="div_data" style="top: 50%;" ><p id="data_head">Total time:</p></div>
	<div style="margin-top: 50px;" id="div_total_time_data">
		<div id="total_time_data"></div>
	</div>

	<div id="div_data" style="left: 230px;" ><p id="data_head">Time to the toilet:</p></div>
	<div id="div_live_timediff">
		<div id="activated_data"></div>
	</div>

	<div id="div_data" style="left: 230px; top: 50%;" ><p id="data_head">Time from the toilet:</p></div>
	<div style="margin-top: 50px;" id="div_live_timediff2">
		<div id="activated_data2"></div>
	</div>
	
	<div id="div_data" style="left: 495px;" ><p id="data_head">Time on the toilet:</p></div>
	<div id="div_live_time_on_toilet">
		<div id="live_time_on_toilet"></div>
	</div>

	<div id="div_data" style="left: 495px; top: 85%" ><p id="data_head">Success rate:</p></div>
	<div id="div_live_made_it">
		<div id="live_made_it"></div>
	</div>

	<div style="bottom: 20px;" class="btn-group">
		
		<a style="font-size: 16px;" href="logout.php" class="btn-group_button">Log ud!</a>
		
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

