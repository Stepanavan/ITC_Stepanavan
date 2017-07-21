var loginArray = ["aaa","sss","ddd","ttt"];
var passArray =["qq","ww","ee","rr"];



var search=function(){
	var inputValue = document.getElementById("firstnameid").value;
	var inputValue1 = document.getElementById("passvordid").value;
	//console.log(inputValue);
	for (i=0;i<loginArray.length;++i){
		for (i=0;i<passArray.length;++i){
		if (inputValue==loginArray[i] && inputValue1==passArray[i]){
			//document.getElementById("searchresult").innerHTML="gf"
			alert("ayo");
		}			
		}
		
	}
	
}