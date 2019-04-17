<?php

function banastexcner_all($result)
{
   while ( ($row = $result->fetch_assoc()) != false) {

      echo "<div class='bolor_grqer col-lg-3'>".
         "<img src='data:image/jpeg;base64,".base64_encode($row["Nkar"])."' alt='cka' >"."<br>".
         "<p class='anun_azganun'>".$row["Anun_Azganun"]."<p>".
      "</div>";


   }
}

$mysqli = new mysqli ("localhost","root","","mybase");
$mysqli->query ("SET NAMES 'utf8' ");
$result = $mysqli->query ('SELECT * FROM `banastexcner`');

banastexcner_all($result);


$mysqli->close();


?>
