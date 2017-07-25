function validate(){
  var password1 = document.getElementById("pass1");
  var confirm_password = document.getElementById("confirm_password");

 if(password1.value != confirm_password.value) {
    
 alert ("Passwords false");
  } else {
  
    alert('password ok');
  }
}


var users = {loreta:"lor", ashot:"ash", emma:"em"};
function stugel() {
  var username = document.getElementById("user").value;
  var password= document.getElementById("pass").value;
 
  for (i in users){
    if (username == i &&  password == users[i]){
      document.getElementById("mutq").style.display = "none";      
      document.getElementById("mutq1").style.display = "block";
      document.getElementById("uname").innerHTML=username;   
      return;
    } else{
      alert("Սխալ մուտք է");
    }
  }
}

var grqer = ["Samvel","Ashot","Anna","Bagrat","Mara","Alla","Vagharsh","Lusine","Jirayr"];
var grqersort=grqer.sort();
function pntrel(){
  
  var a = document.getElementById("search1").value;
  for (var i = 0; i < grqer.length; i++) {
    if (grqer[i] == a){
      alert("Գիրքն առկա է");
      return 0;
    }    
  }
  alert("Այս պահին տվյալ գիրքը չկա");
}
