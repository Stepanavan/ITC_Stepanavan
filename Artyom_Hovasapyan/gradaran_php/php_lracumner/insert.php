<?php

   $mysqli = new mysqli ("localhost","root","","mybase");
   $mysqli->query ("SET NAMES 'utf8' ");

   $anun_ = $_POST['anun_storage'];
   $azganun_ = $_POST['azganun_storage'];
   $phone_ = $_POST['phone_storage'];
   include 'result_patmakan.php';


   $url = $_SERVER['REQUEST_URI'];
   $position_anun = strrpos( $url,'banastexc_anun=' );
   $position_azganun = strrpos( $url,'banastexc_azganun=' );

if ( $anun_ != null and $azganun_ != null and $phone_ != null) {

   if ( $_POST['tip_banastexc'] == 'Patmakan') {
      $result = $mysqli->query ("SELECT * FROM `users` WHERE Banastexcutyan_tip = 'patmakan' ");
   }
   else if ( $_POST['tip_banastexc'] == 'Gexarvestakan') {
      $result = $mysqli->query ("SELECT * FROM `users` WHERE Banastexcutyan_tip = 'gexarvestakan' ");
   }
   else if( $url ){
      $url_stugum = $_POST['url_stugum'];
      $b_anun = $_POST['b_anun'.$url_stugum];
      $b_azganun = $_POST['b_azganun'.$url_stugum];

      $result = $mysqli->query ("SELECT * FROM `users` WHERE Anun = '$b_anun' and Azganun = '$b_azganun' ");
   }

   $stugum = $_POST["stugum"];

   // vorpesi banastexcner_all funkciayum karoxanam ogtagorcem
   $ka_girg = $_POST['grqi_qanank'.$stugum];
   $vernagiri_stugum = $_POST['vernagir'.$stugum];
   $btn_stugum = $_POST["send".$stugum];
   $patvirel_cexarkel_stugel = $_POST['bulian'.$stugum];

   $banastexci_anun = $_POST["banastexci_anun_".$stugum];
   $banastexci_azganun = $_POST["banastexci_azganun_".$stugum];


   function banastexcner_all($result)
   {

         $count = 0;

         while ( ($row = $result->fetch_assoc()) )
         {
            if(( $GLOBALS['ka_girg']  ==  $row['grqi_qanank'] ) and
               ( $GLOBALS['vernagiri_stugum']  ==  $row['Banastexcutyan_vernagir'] ) and
               ( $GLOBALS['stugum']  ==  $count )
              ){
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
      $mysqli->query("INSERT INTO `u` ( ANUN, AZGANUN, PHONE, banastexci_anun, banastexci_azganun, girg ) VALUES
         ('$anun_','$azganun_','$phone_','$banastexci_anun','$banastexci_azganun','$vernagiri_stugum' ) ");
      echo 'Der Patver@ katarvace';



   }

   elseif ( $patvirel_cexarkel_stugel == 'false' )
   {
      $mysqli->query("UPDATE `users` SET grqi_qanank = $ka_girg + 1 WHERE Banastexcutyan_vernagir = '".$vernagiri_stugum."'");
      $mysqli->query("DELETE FROM `u` WHERE ( ANUN = '$anun_' and AZGANUN = '$azganun_' and PHONE = '$phone_'  and
                     banastexci_anun = '$banastexci_anun' and banastexci_azganun = '$banastexci_azganun' and girg = '$vernagiri_stugum' )");
      echo 'Der Patver@ cexarkvace';


   }
   else {
      echo 'sxal mutg';
   }
}



   $mysqli->close();


 ?>
