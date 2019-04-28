<div class="form-popup" id="myForm">
  <div class="form-container">
   <h1>Login</h1>

   <label for="Anun"><b>Anun</b></label>
   <input id="anun_" type="text" placeholder="Der anuny" name="anun_" required>

   <label for="Aganun"><b>Aganun</b></label>
   <input id="azganun_" type="text" placeholder="Der Aganun" name="azganun_" required>

   <label for="Heraxos"><b>Heraxos</b></label>
   <input id="phone_" type="text" placeholder="Der HEraxosahamar@" name="phone_"  required>

   <a id='uxarkel_btn' type="submit" class="btn" name = 'btn_login' value="atpravit">uxarkel</a>
   <input type="hidden" name="anun_storage" id="anun_storage">
   <input type="hidden" name="azganun_storage" id="azganun_storage">
   <input type="hidden" name="phone_storage" id="phone_storage">

   <button type="button" class="btn cancel" onclick="closeForm()">Close</button>

</div>
</div>

<script>


var anun_storage = localStorage.getItem( "login_storage_anun" );
var azganun_storage = localStorage.getItem( "login_storage_azganun" );
var phone_storage = localStorage.getItem( "login_storage_phone" );


document.getElementById('anun_storage').value = anun_storage;
document.getElementById('azganun_storage').value = azganun_storage;
document.getElementById('phone_storage').value = phone_storage;

var uxarkel_btn = document.getElementById('uxarkel_btn');
uxarkel_btn.onclick = function()
{
   var id_anun = document.getElementById('anun_').value;
   var id_azganun = document.getElementById('azganun_').value;
   var id_phone = document.getElementById('phone_').value;

   if( (id_anun != "") && (id_azganun != "") && (id_phone != "") ){
      localStorage.setItem( "login_storage_anun", id_anun);
      localStorage.setItem( "login_storage_azganun", id_azganun);
      localStorage.setItem( "login_storage_phone", id_phone);

      document.getElementById('anun_storage').value = localStorage.getItem( "login_storage_anun");
      document.getElementById('azganun_storage').value = localStorage.getItem( "login_storage_azganun");
      document.getElementById('phone_storage').value = localStorage.getItem( "login_storage_phone");
      closeForm();
   }
   else {
      openForm();
   }

}
   function openForm() {

      var anun_storage = localStorage.getItem( "login_storage_anun" );
      var azganun_storage = localStorage.getItem( "login_storage_azganun" );
      var phone_storage = localStorage.getItem( "login_storage_phone" );

      if( (anun_storage == null) || (azganun_storage == null) || (phone_storage == null) )
         document.getElementById("myForm").style.display = "block";
   }

   function closeForm() {
     document.getElementById("myForm").style.display = "none";
   }


</script>
