var color;
function colorizer(a){
  color=  document.getElementById(a.id).style.backgroundColor;
    
}

function x(a){
//document.getElementById(a.id).style.backgroundColor=document.getElementById('select').value;
    document.getElementById(a.id).style.backgroundColor=color;
console.log(color);
}

function colorizer(){
	click=true;
}
function uncolorizer(){

	click=false;
}