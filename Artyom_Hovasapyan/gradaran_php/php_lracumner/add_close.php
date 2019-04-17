<?php
$t=$_POST['3'];
echo $t;

$mysqli = new mysqli ("localhost","root","","mybase");
$mysqli->query ("SET NAMES 'utf8' ");
$result = $mysqli->query ("SELECT * FROM `users` WHERE (Banastexcutyan_tip = 'patmakan' or Banastexcutyan_tip = 'Patmakan' )");
$r=0;
while ( ($row = $result->fetch_assoc()) != false) {
   if( ($t==$row['grqi_qanank'] ) && ($r=='3'))
   {
      echo($row['grqi_qanank']." ddddddddddd ");
      break;
   }
   $r++;
}
echo "  ".$r;

$mysqli->close();


?>
