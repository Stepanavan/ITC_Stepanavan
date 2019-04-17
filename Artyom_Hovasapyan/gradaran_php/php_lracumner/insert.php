<?php

   $mysqli = new mysqli ("localhost","root","","mybase");
   $mysqli->query ("SET NAMES 'utf8' ");

   if ( $_POST['tip_banastexc'] == 'Patmakan') {
      $result = $mysqli->query ("SELECT * FROM `users` WHERE Banastexcutyan_tip = 'patmakan' ");
   }
   else if ( $_POST['tip_banastexc'] == 'Gexarvestakan') {
      $result = $mysqli->query ("SELECT * FROM `users` WHERE Banastexcutyan_tip = 'gexarvestakan' ");
   }


   $stugum = $_POST["stugum"];

   // vorpesi banastexcner_all funkciayum karoxanam ogtagorcem
   $ka_girg = $_POST['grqi_qanank'.$stugum];
   $vernagiri_stugum = $_POST['vernagir'.$stugum];
   $btn_stugum =  $_POST["send".$stugum];
   $patvirel_cexarkel_stugel = $_POST['bulian'.$stugum];

   function banastexcner_all($result)
   {

      $count = 0;
      while ( ($row = $result->fetch_assoc()) )
      {
         if(( $GLOBALS['ka_girg']  ==  $row['grqi_qanank'] ) and
            ( $GLOBALS['vernagiri_stugum']  ==  $row['Banastexcutyan_vernagir'] ) and
            ( $GLOBALS['stugum']  ==  $count )
           )
         {
            if( $GLOBALS['patvirel_cexarkel_stugel'] == 'false' )
            {
               $GLOBALS['patvirel_cexarkel_stugel'] = 'true';
            }else {
               $GLOBALS['patvirel_cexarkel_stugel'] = 'false';
            }

            return;
         }
         $count++;

      }
   }


   banastexcner_all($result);


   if ( $patvirel_cexarkel_stugel == 'true' and $ka_girg > 0 )
   {
      $mysqli->query("UPDATE `users` SET grqi_qanank = $ka_girg - 1 WHERE Banastexcutyan_vernagir = '".$vernagiri_stugum."'");
      echo 'Der Patver@ katarvace';
   }

   elseif ( $patvirel_cexarkel_stugel == 'false' )
   {
      $mysqli->query("UPDATE `users` SET grqi_qanank = $ka_girg + 1 WHERE Banastexcutyan_vernagir = '".$vernagiri_stugum."'");
      echo 'Der Patver@ cexarkvace';
   }
   else {
      echo 'sxal mutg';
   }



   $mysqli->close();


 ?>
