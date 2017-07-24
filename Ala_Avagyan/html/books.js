//objects for books names
var booksNames=[
  {
	  author:"Հովհաննես Թումանյան",
	  creation:"Գիքոր"
  },
 {
	  author:"Ավետիք Իսահակյան",
	  creation:"Աբու լալա Մահարի"
  }

];
//function for searching for books
var search = function() { 
    var para = document.getElementById("author").value;
    var creat = document.getElementById("creation").value;
	
   console.log(para);
   for (var j = 0; j < booksNames.length; j++) {
	   if (para === booksNames[j].author && creat==booksNames[j].creation) {
		  alert("Գիրքը գտնված է");
			return 0;		  
      }
   } 
		alert("Գիրքը չի գտնվել");   
}
//objects for users
var ObjPeople=[
  {
	user:"Ala",
	pass:"111"
  },
{
	user:"Ani",
	pass:"222"	
  },
{
	user:"Ara",
	pass:"333"
  },
{
	user:"Ana",
	pass:"444"
  }
];

//function for users logg in
function Clicked(){
	var user1 = document.getElementById("user").value;
	var pass1 = document.getElementById("pass").value;		
	for(i=0; i<ObjPeople.length;i++){
		console.log(user1);
		console.log(pass1);
		if(user1==ObjPeople[i].user && pass1==ObjPeople[i].pass){
			document.getElementById('peoples').innerHTML="Դուք հաջողությամբ մուտք եք գործել";
			return 0;
		}
	}
	document.getElementById('peoples').innerHTML="Սխալ անուն կամ Ծածկագիր";
}