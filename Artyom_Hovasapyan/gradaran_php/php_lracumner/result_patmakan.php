<?php

   $url = $_SERVER['REQUEST_URI'];
   $b = "";


   for ( $j = 0,$i = strlen($url)-5; $i > 0 ; $i--, $j++) {
      if( $url[$i] != '/'){
         $b .= $url[$i];
      }
      else {
         break;
      }
   }

   $b = strrev($b);

   if($b == 'patmakan' or $b == 'Patmakan'){
      $result = $mysqli->query ("SELECT * FROM `users` WHERE Banastexcutyan_tip = 'patmakan' ");
   }
   elseif($b == 'gexarvestakan' or $b == 'Gexarvestakan'){
      $result = $mysqli->query ("SELECT * FROM `users` WHERE Banastexcutyan_tip = 'gexarvestakan' ");
   }



 ?>
