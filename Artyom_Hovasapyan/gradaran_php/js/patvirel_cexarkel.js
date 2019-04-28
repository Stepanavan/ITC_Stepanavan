// localStorage Patvirel_chexarkel ||   mekel ajaxi mej ka migani tox

var url_link = '';
var str = document.URL;


if ( str.indexOf("Patmakan") >= 0 ) {
  str = 'patmakan';
}
else if ( str.indexOf("Gexarvestakan") >= 0 ) {
   str = 'gexarvestakan';
}

for ( var i = 0; i < i+1; i++ ) {
   var cookie_bool = localStorage.getItem(str+'_btn_type'+i);
   try {
      if( cookie_bool == null ){

         localStorage.setItem( str+'_btn_type'+i,'false' );
         document.getElementById( "bulian"+i).value = 'false';
      }
      else if ( cookie_bool !== null ) {
         document.getElementById("bulian"+i).value = cookie_bool;
         if(cookie_bool == 'true'){
            document.getElementsByClassName('send')[i].innerHTML = "Cexarkel";
            document.getElementsByClassName('send')[i].style.background = "red";
         }
      }
   }
   catch (e)
   {
      break;
   }

}



// end localStorage Patvirel_chexarkel
