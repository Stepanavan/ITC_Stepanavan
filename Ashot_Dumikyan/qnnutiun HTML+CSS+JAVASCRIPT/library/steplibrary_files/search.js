
var book = ['January', 'February' , 'March'];

function books(){
	var bookname = document.getElementById("bookin").value;
	var x=document.getElementById("container")
	if ( book.indexOf( bookname ) != -1 ){
		alert("Ձեր կողմից փնտրած  "+bookname+"  գիրքը գրադարանում առկա է");
		x.style.zIndex=-2;
	}else
		alert("Ձեր կողմից փնտրած  "+bookname+"  գիրքը գրադարանում բացակայում է")
	//console.log(bookname);
}



