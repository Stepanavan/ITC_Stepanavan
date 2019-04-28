<head>
   <link rel="stylesheet" href="css/banastexcner.css">
   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
       crossorigin="anonymous">
</head>
<header class="container">
<div class="" style="display:flex;" >
</header>
<body>

<form>
   <div class="nav d-flex" style="justify-content:center">
      <?php include 'php_lracumner/menak_banastexcner.php'; ?>
   </div>
   <div class="" hidden>
      <input id="stugum" type="text" name="stugum" value="">
   </div>
   <?php include "php_lracumner/login_storage.php"; ?>
</form>

</body>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"> </script>

<!--  localStorage Patvirel_chexarkel ||   mekel ajaxi mej ka migani tox-->
<script type="text/javascript" src="js/patvirel_cexarkel.js"></script>
<!--  end localStorage Patvirel_chexarkel -->

<script>

function btn_click(){

      var a = event.target.getAttribute("name");
      document.getElementById('stugum').value = a;
      var dannie = $('form').serialize();

      $.ajax({
         url:'php_lracumner/insert.php',
         type:'POST',
         data: dannie,
         success:function(data) {
            alert(data);

            localStorage.setItem( str+'_btn_type'+a, document.getElementById("bulian"+a).value );
            var localValue = localStorage.getItem( str+'_btn_type'+a );

            if( data == 'Der Patver@ katarvace' ){
               alert( 'Patvere@ katarvac e' );
               if(localValue == 'false')
               {
                  document.getElementById( "bulian"+a ).value = 'true';
                  localStorage.setItem(str+'_btn_type'+a, 'true');
               }
               var d = Date();
               localStorage.setItem( str+'_time_'+a, d );

               document.getElementsByClassName('send')[a].innerHTML = "Cexarkel";
               document.getElementsByClassName('send')[a].style.background = "red";
               document.getElementById('tiv_'+a).innerHTML -= 1;
               document.getElementById("grqi_qanank"+a).value -= 1;

            }

            else if ( data == 'Der Patver@ cexarkvace' ) {
               alert('Patvere@ cexarkvace');

               if(localValue == 'true')
               {
                  document.getElementById("bulian"+a).value = 'false';
                  localStorage.setItem(str+'_btn_type'+a, 'false');
               }

               localStorage.removeItem( str+'_time_'+a);
               document.getElementById('anun_'+a).type = 'hidden';

               document.getElementsByClassName('send')[a].innerHTML = "Patvirel";
               document.getElementsByClassName('send')[a].style.background = "green";
               document.getElementById('tiv_'+a).innerHTML -= -1;
               document.getElementById("grqi_qanank"+a).value -= -1;

            }

            else {
               alert('Ays pahin ceg karox');
            }


         }
      })

}

</script>
