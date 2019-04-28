<?php

function banastexcner_($result)
{
   $count = 0;
   while ( ($row = $result->fetch_assoc()) != false) {

      echo "
      <div class='bolor_grqer col-lg-3'>".
      "<form method='GET'>
         <button id='btn_stugum_banastexc' onclick='url_stugum()' name='send' class='anun_azganun_nkar' >".
            "<img src='data:image/jpeg;base64,".base64_encode($row["Nkar"])."' alt='cka' name='".$count."'>".
            "<span class='anun_azganun' name='".$row["Anun"]."'>".$row["Anun"]." </span>".
            "<span class='anun_azganun' name='".$row["Azganun"]."'>".$row["Azganun"]."</span>".
         "</button>".
      "
       <input id='banastexcner_anun_azganun' type='text' name='banastexc_anun' value='".$row["Anun"]."' hidden>
       <input id='banastexcner_anun_azganun' type='text' name='banastexc_azganun' value='".$row["Azganun"]."' hidden>
       <input id='b_anun_azganun' type='text' name='b_anun".$count."' value='".$row["Anun"]."' hidden>
       <input id='b_anun_azganun' type='text' name='b_azganun".$count."' value='".$row["Azganun"]."' hidden>

      </form>
      </div>";

      $count++;

   }

}

$mysqli = new mysqli ("localhost","root","","mybase");
$mysqli->query ("SET NAMES 'utf8' ");
$result = $mysqli->query ('SELECT * FROM `banastexcner`');

banastexcner_($result);


$mysqli->close();


?>
