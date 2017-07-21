var loginArray = ["aaa","sss","ddd","ttt"];
var passArray =["qq","ww","ee","rr"];
var booksArray=["samvel","giqor","eraz"];


var search=function(){
	var inputValue = document.getElementById("firstnameid").value;
	var inputValue1 = document.getElementById("passvordid").value;
	//console.log(inputValue);
	for (i=0;i<loginArray.length;++i){
		if (inputValue==loginArray[i] && inputValue1==passArray[i]){
			//document.getElementById("searchresult").innerHTML="gf"
			alert("ayo");
		}				
	}
}




var my=function(){
	var booksValue = document.getElementById("searchinput").value;
	//console.log(booksValue);
	for (i=0;i<booksArray.length;++i){
		if (booksValue==booksArray[i]) {
			document.getElementById("searchresult").innerHTML="Girq@ gta";
	
		}				
	}
}
