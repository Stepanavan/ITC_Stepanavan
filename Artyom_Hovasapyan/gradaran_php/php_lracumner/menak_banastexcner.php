<?php

   $mysqli = new mysqli ("localhost","root","","mybase");
   $mysqli->query ("SET NAMES 'utf8' ");
   include 'result_patmakan.php';
   function banastexcner_all($result)
   {

      $count=0;
      $tip_banastexc = $GLOBALS['b'];
      while ( ($row = $result->fetch_assoc()) != false)
      {
         echo "<div id='send".$count."' class='bolor_grqer col-lg-3' >".
            "<img src='data:image/jpeg;base64,".base64_encode($row["Nkar"])."' alt='cka' >"."".
            "<p class='anun_azganun cursor-pointer'>".$row["Anun"]." ".$row["Azganun"]."</p>".
            "<p class='cursor-pointer'><< ".$row["Banastexcutyan_vernagir"].">>
               <input name='vernagir".$count."' value='".$row["Banastexcutyan_vernagir"]."'  hidden>
            </p> ".
            " <p class=''><span id='tiv_".$count."' class='tiv_'>".
               $row["grqi_qanank"]."</span>
               <input id='grqi_qanank".$count."' type='hidden' name='grqi_qanank".$count."' value='".$row["grqi_qanank"]."' >
                  -hat azat girq ka ".
               "<p>
                  <a type='submit' class='send' id='send' onclick='btn_click();' name='".$count."' >Patvirel</a>
                  <input type='hidden' name='send".$count."' value='".$count."' >
                  <input id='bulian".$count."' type='hidden' name='bulian".$count."' value='false' >
                  <input type='hidden' name='tip_banastexc' = something;' value='$tip_banastexc'  >
               </p>".
            "</p>".
         "</div>";
         $count++;

      }
   }

   banastexcner_all($result);

   $mysqli->close();

?>
