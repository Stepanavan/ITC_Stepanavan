<!DOCTYPE html>
<head>
<title>new</title>
<meta charset="UTF-8">
<style>
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
</style>

</head>


<body>

<?php

	$x = 1;
	 
	while ($x <= 50) {
	   echo "<p>Этот текст повторяется 50 раз</p>";
	   $x = $x + 1;
	}
	?>

<table style="width:100%">
  <tr>
    <th>Անուն</th>
    <th>Ազգանուն</th> 
    <th>տարիք</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td>
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td>
    <td>94</td>
  </tr>
  <tr>
    <td>John</td>
    <td>Doe</td>
    <td>80</td>
  </tr>
</table>

 

</body>
</html>
