<?php

   $url = $_SERVER['REQUEST_URI'];
   $position_anun_stugum = strrpos( $url,'banastexc_anun=' );
   $b = "";
   $pos = '';
   global $result;
   $groxi_anun = "";
   $groxi_azganun = "";

   for ( $j = 0,$i = strlen($url)-5; $i > 0 ; $i--, $j++) {
      if( $url[$i] != '/'){
         $b .= $url[$i];
      }
      else {
         break;
      }
   }

   $pos = stristr($url, 'b');
   $pos = substr($pos, 0, 12);

   $b = strrev($b);

   if( $b == 'patmakan' or $b == 'Patmakan'){
      $GLOBALS['result'] = $mysqli->query ("SELECT * FROM `users` WHERE Banastexcutyan_tip = 'patmakan' ");
   }
   elseif( $b == 'gexarvestakan' or $b == 'Gexarvestakan'){
      $GLOBALS['result']= $mysqli->query ("SELECT * FROM `users` WHERE Banastexcutyan_tip = 'gexarvestakan' ");
   }
   elseif( $pos == 'banastexcner') {
      if(isset( $_GET['send'] )){

         // tver@ banastexc_anun lneght u banastexc_azganun lenght
         // stuguma animast gic mic zhdni
         // karelia naev nergevi forer@ funciaov anel

         $url = $_SERVER['REQUEST_URI'];
         $position_anun = strrpos( $url,'banastexc_anun=' );
         $position_azganun = strrpos( $url,'banastexc_azganun=' );

         for ( $i = $position_anun+15; $i < $position_azganun-1; $i++ ) {
            $ascii = true;
            for ( $j = 33; $j < 65; $j++ ) {
               if( $url[$i] == chr($j) ){
                  $ascii = false;
                  break;
               }
            }
            if( $ascii )
               $GLOBALS['groxi_anun'] .= $url[$i];
            else {
               break;
            }
         }

         for ( $i = $position_azganun+18; $i < strlen( $url ) ; $i++ ) {
            $ascii = true;
            for ( $j = 33; $j < 65; $j++ ) {
               if( $url[$i] == chr($j) ){
                  $ascii = false;
                  break;
               }
            }
            if( $ascii )
               $GLOBALS['groxi_azganun'] .= $url[$i];
            else {
               break;
            }
         }

         $groxi_anun = $GLOBALS['groxi_anun'];
         $groxi_azganun = $GLOBALS['groxi_azganun'];

         $result = $mysqli->query ("SELECT * FROM `users` WHERE Anun = '$groxi_anun' and Azganun = '$groxi_azganun' ");
      }


   }





// $GLOBALS['result'] = $mysqli->query ("SELECT * FROM `users` WHERE Anun = '$a' ");

// $GLOBALS['result'] = $mysqli->query ("SELECT * FROM `users` WHERE Anun = 'artyom' ");

//  es depgum linuma
// $GLOBALS['result'] = $mysqli->query ("SELECT * FROM `users` WHERE Anun = '$groxi_anun' and Azganun = '$groxi_azganun' ");




 ?>
