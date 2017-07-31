
function Z(){
var i=0;
var j=2;
var elem=document.getElementById('animated');
setInterval(function (){

   i+=j
    if (i==100){
         j=-2;
       
        
    }
    if (i==-100){
        j=2;
        
    }   
        
    console.log(i);
     
    document.getElementById('animated').style.marginLeft=i+"px";
    document.getElementById('animated').style.width=i+"px";
    document.getElementById('animated').style.marginRight=i+"px";
   

    
 
}, 1000/60 );




}
