form.onsubmit = function(e){
    e.preventDefault();
}

document.getElementById('abutton').onclick=function(e){
var login=document.getElementById('login');
var passwor=document.getElementById('password');  

    if(parseInt(login.value)){
        login.style.border="1px solid red";
        
        return 0;
    }
    if(String(login.value)){
        alert("nice");
        return 0;
    }
    if(parseInt(password.value)){
        password.style.border="1px solid red";
        return 0;
    }
    if(String(password.value)){
        alert("nice");
        return 0;
    }
  
  
    
    
};

