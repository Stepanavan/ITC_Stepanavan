
var loginarray = [{login:"aaa",pass:"zz"},{login:"sss",pass:"xx"},{login:"ddd",pass:"cc"},{login:"fff",pass:"vv"}];

var login=function(){
	var loginValue = document.getElementById("firstnameid").value;
	var passValue = document.getElementById("passwordid").value;
	console.log(loginValue);
	
	for (var i =0;i< loginarray.length;++i){

		if (loginValue==loginarray[i].login && passValue==loginarray[i].pass){
			
				alert("Barev");
				return;
			} else if (loginValue==loginarray[i].login && passValue!=loginarray[i].pass){
				alert("pass@ sxal E");
				return;
			}
	}
	alert("login  sxal E");
}


var booksArray=["samvel","giqor","eraz"];

var search=function(){
	var booksValue = document.getElementById("searchinput").value;
	console.log(booksValue);
	for (var i=0 ;i< booksArray.length;++i){
		console.log(booksArray[i]) ;
		if (booksValue==booksArray[i]) {
			//console.log(booksArray) ;
			document.getElementById("searchresult").innerHTML="Girq@ gta";
			return;
		}
	}
	document.getElementById("searchresult").innerHTML="Girq@ chgta";
}
var mutq=function(){
	location.assign("mutq.html");
}
