//console.log("Page changed")

function clickChecker(){
	console.log("chekced will be done");
}








var users;




var autoLogin = function (){
	
	
	
	users = [
		
	{
	log:'ar2r',
	pass:'ar2r',
	name:'Ar2r_Papian',
	img:'image/users/YourLogoHere.jpg'
	},{
	log:'2',
	pass:'ar2r',
	name:'2',
	img:'image/users/YourLogoHere.jpg'
	},{
	log:'3',
	pass:'3',
	name:'3',
	img:'image/users/YourLogoHere.jpg'
	},
		
		{
	log:'4',
	pass:'4',
	name:'4',
	img:'image/users/YourLogoHere.jpg'
	}
				 
	];
	


	
	
	
	var profile=document.getElementById('profile');
	var auth=document.getElementById('auth');

	
	
	/*	REGISTRATION PLACE*/
	var newlog='10';
	var newpass='10';
	var newname='10';
	var newimg='image/users/ar2r.jpg';

	users.push({log:newlog,pass:newpass,name:newname,img:newimg});

	//console.log(users)
	
	
	var userphoto=document.getElementById('userimg');
	var username=document.getElementById('username');
	
	for (var i=0; i < users.length; ++i){
		//console.log(localStorage.getItem(users[i].log),users[i].pass);
		var x=0
		if(localStorage.getItem(users[i].log) === users[i].pass){
				//console.log('work');
				username.innerHTML=users[i].name;
				userphoto.setAttribute('src', users[i].img);
				autentification();
				//document.getElementById('auth').style.display='none';
				x=1
				break;			
		}	

	}

	if(x == 1){
			console.log('work2');
			auth.style.display='none';
			
		}
	if(x !== 1){
		profile.style.display='none';
	}
}();




	

function logout(){
	//console.log('logout');
	localStorage.clear();
	for (var i=0; i<users.length; ++i){          
  				localStorage.removeItem(users[i].log);

	}
	unAutentification();
	setTimeout(function(){location.reload()},1000);
	document.getElementById('profile').style.display='none'
}





function login(){        
		var auth;           
		var log = document.getElementById('logininput').value;   
		var pass= document.getElementById('passwordinput').value;  
		var checklog=[];  			 
		var checkpass=[];
		for (var i=0; i<users.length; ++i){          
  				
			checklog.push(users[i].log);
			checkpass.push(users[i].pass);
			
			
		}
		if ( checklog.indexOf( log ) != -1 ){
			alert("Login ready");
			if ( checkpass.indexOf( pass ) != -1 ){
				alert("Pass ready");
				autentification();              
				localStorage.setItem(log, pass);  
			}else{
				alert("Password Wrong")
			}
		}	
		else{
		alert("Login Wrong")
	
}
	
	
	console.log(checklog,checkpass)
	setTimeout(function(){location.reload()},1000);
	}	
			
		
		







/*document.getElementById('logoutbtn').onclick= function(){
	localStorage.clear();
	console.log('dsa')
	setTimeout(function(){location.reload()},1000);
for (var i=0; i < users.length; ++i){
			var remove = users[i].log 
			localStorage.removeItem(users[i].log);
			unAutentification();
			setTimeout(function(){location.reload()},1000);
			
		
	}

}*/




/*            LOGIN              */




/*
document.getElementById('loginbtn').onclick=function(){
var user = document.getElementById('logininput').value;
var pass= document.getElementById('passwordinput').value;
	setTimeout(function(){
				location.reload() },1000);


					
			}
	
	for (var i=0; i<users.length; ++i){
		var checklog = users[i].log;
		var checkpass = users[i].pass;
		console.log(checklog, checkpass)
		if( checklog==user && checkpass == pass)
			{

				autentification();
				localStorage.setItem(checklog, checkpass);
				
		
	}

	
}
*/




var l = false;
function openLoginMenu(){
	if(!l){
	document.getElementById('loginframe').style.display='block';
	document.getElementById('regframe').style.display='none';
	p=false;
	l=true;
	}
	
	else{
	document.getElementById('loginframe').style.display='none';
	l=false;
	}
}



function autentification(){
	var el = document.getElementById('auth');
	el.parentNode.removeChild(el);
}

function unAutentification(){
	var el = document.getElementById('profile');
	el.parentNode.removeChild(el);
	
}





/*
document.getElementById('login').onclick=function(){
	
	
	if(!l){
	document.getElementById('loginframe').style.display='block';
	document.getElementById('regframe').style.display='none';
	p=false;
	l=true;
	}
	
	else{
	document.getElementById('loginframe').style.display='none';
	l=false;
	}
}
*/
var p = false;
function openRegisterMenu(){
		if(!p){
	document.getElementById('regframe').style.display='block';
	document.getElementById('loginframe').style.display='none';
	l=false;
	p=true;
	}
	
	else{
	document.getElementById('regframe').style.display='none';
	p=false;
	}
	
	
}


/*document.getElementById('password').onclick=function(){
	
	
	if(!p){
	document.getElementById('regframe').style.display='block';
	document.getElementById('loginframe').style.display='none';
	l=false;
	p=true;
	}
	
	else{
	document.getElementById('regframe').style.display='none';
	p=false;
	}
}*/






function openLeftMenu(){
	var menu = document.getElementById('menu');
	if (!menu.classList.contains('menushow')) {
		 console.log(1);
        menu.classList.add('menushow');
		document.getElementById('openmenu').style.transform="rotateY(180deg)"
      }else{
		  menu.classList.remove('menushow');
		  document.getElementById('openmenu').style.transform="rotateY(0deg)"
		  console.log(2);
	  }
	
	
}





/*document.getElementById('openmenu').onclick=function(){
	var menu = document.getElementById('menu');
	if (!menu.classList.contains('menushow')) {
		 console.log(1);
        menu.classList.add('menushow');
		document.getElementById('openmenu').style.transform="rotateY(180deg)"
      }else{
		  menu.classList.remove('menushow');
		  document.getElementById('openmenu').style.transform="rotateY(0deg)"
		  console.log(2);
	  }
	
}*/

function openRightMenu(){
	var menu = document.getElementById('categories');
	if (!menu.classList.contains('categoriesshow')) {
		document.getElementById('opencategories').style.transform="rotateY(0deg)"
		 console.log(1);
        menu.classList.add('categoriesshow');
      }else{
		  document.getElementById('opencategories').style.transform="rotateY(180deg)"
		  menu.classList.remove('categoriesshow');
		  console.log(2);
	  }
	
}


/*document.getElementById('opencategories').onclick=function(){
	var menu = document.getElementById('categories');
	if (!menu.classList.contains('categoriesshow')) {
		document.getElementById('opencategories').style.transform="rotateY(0deg)"
		 console.log(1);
        menu.classList.add('categoriesshow');
      }else{
		  document.getElementById('opencategories').style.transform="rotateY(180deg)"
		  menu.classList.remove('categoriesshow');
		  console.log(2);
	  }
	
}*/



/*window.onclick = function(event) {
  if (!event.target.matches('#menu') && !event.target.matches('#openmenu')) {

   	document.getElementById('menu').classList.remove('menushow');
	document.getElementById('openmenu').style.transform="rotateY(0deg)"
		

  }
	  if (!event.target.matches('#opencategories') && !event.target.matches('#categories') ) {
		  if( !event.target.matches('#searchinput') && !event.target.matches('div#site'))
			  if(!event.target.matches('#searchresult'))
				  if(!event.target.matches('span.ng-binding')){
						document.getElementById('categories').classList.remove('categoriesshow');
						document.getElementById('opencategories').style.transform="rotateY(180deg)"
				  }
		 

  }
	


}*/



var canvas = document.getElementById("textSlider");
var ctx = canvas.getContext("2d");



var textDataBase=[ "Your text 1 ","Your text 2 ", "Your text 3 ", "Your text 4 ", "Your text 5 " ]  


	ctx.fillStyle = "saddlebrown";
   
    ctx.font = "15pt Verdana";
   
 var x = 900;
	
 var itext = 0
 var sliding = function() {
	ctx.clearRect(0,0,1000,20);
	ctx.fillText(textDataBase[itext], x, 15);
	x-=1;
	//console.log(x);
	if (x == -300){ 
		x = 900;
		++itext;
	}
	 if(itext == textDataBase.length) itext = 0;
	 
	
}




var loop = setInterval(function(){
	sliding();

} ,25);






