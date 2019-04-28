// banastexcner@ stugumeng 
function url_stugum() {
   var a = document.getElementById('btn_stugum_banastexc');
   localStorage.setItem('btn_type_banastexcner',event.target.name);
   document.getElementById('url_stugum').value = localStorage.getItem('btn_type_banastexcner');
   $('.anun_azganun_nkar').hide();
}
document.getElementById('url_stugum').value = localStorage.getItem('btn_type_banastexcner');
