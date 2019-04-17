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
</form>

</body>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"> </script>

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

            if( data == 'Der Patver@ katarvace' ){
               alert('Patvere@ katarvac e');
               document.getElementsByClassName('send')[a].innerHTML = "Cexarkel";
               document.getElementsByClassName('send')[a].style.background = "red";
               document.getElementById('tiv_'+a).innerHTML -= 1;
               document.getElementById("grqi_qanank"+a).value -= 1;
               document.getElementById("bulian"+a).value = "true";
            }
            else if ( data == 'Der Patver@ cexarkvace' ) {
               alert('Patvere@ cexarkvace');
               document.getElementsByClassName('send')[a].innerHTML = "Patvirel";
               document.getElementsByClassName('send')[a].style.background = "green";
               document.getElementById('tiv_'+a).innerHTML -= -1;
               document.getElementById("grqi_qanank"+a).value -= -1;
               document.getElementById("bulian"+a).value = "false";

            }
            else {
               alert('Ays pahin cka');
            }


         }
      })

}

</script>
