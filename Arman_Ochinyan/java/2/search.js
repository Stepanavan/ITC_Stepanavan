var loginArray = {aaa:"zz",sss:"xx",ddd:"cc",fff:"vv"};
//var passArray =["qq","ww","ee","rr"];
var booksArray=["samvel","giqor","eraz"];


var my=function(){
	var inputValue = document.getElementById("firstnameid").value;
	var inputValue1 = document.getElementById("passwordid").value;
	//console.log(inputValue);
	for (var i in loginArray){
		if (inputValue==i && inputValue1==loginArray[i]){
			alert("Barev");
		}				
	}
}

var search=function(){
	var booksValue = document.getElementById("searchinput").value;
	//console.log(booksValue);
	for (i=0;i<booksArray.length;++i){
		if (booksValue==booksArray[i]) {
			document.getElementById("searchresult").innerHTML="Girq@ gta";
		}				
	}
}

var mutq= function(){
	window.location.assign("mutq.html")
	
}
