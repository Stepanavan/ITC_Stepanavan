var target = document.getElementById('target');
var path = 30 ;
var bullet=document.getElementById('bullet');
var player=document.getElementById('player');

var qayl=50;

var path1=0;
var qayl1=50;

document.onkeydown=function(e){
   console.log(e.key)
    if( e.key == "ArrowLeft" ){
      
        path1+=50;
        console.log(path1);
        player.style.right=path1+ qayl1+'px';
       
  
        
    }
    if( e.key == "ArrowRight" ){
        
        path1-=50;
      console.log(path1);
        player.style.right=path1+qayl1+'px';
       
        
        
    }
    if(e.key==" "){
        console.log('SPACE')
        shoot();

    }

    
}

    

    target.onload=function(){

    game();

    }
     var game = setInterval(function(){
         
        if (path>90){
              console.log(1);
            qayl=-5;
         }
         if (path<=-30){
             qayl=5;
              console.log(2);
             }
         path+=qayl;

        target.style.left= path+'%';

       } ,100 );

        

    function shoot(){
        bullet.style.top=-700+'px';

        timer = setInterval(function(){

            bullet.style.display='none';    
            

            },250);


            timer1 = setInterval(function(){
                bullet.style.top=0+'px';
                bullet.style.display='block';    
             



            },250);

        sss = setTimeout(function(){
        clearInterval(timer);
        clearInterval(timer1);
        clearTimeout(sss)

        }
        ,1000)

    }    
        