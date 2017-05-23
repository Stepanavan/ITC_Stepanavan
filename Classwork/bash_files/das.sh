#!/bin/bash
function cin
{
  while [ $B != ${map[$B]} ]
  do 
   echo ""
    read -n 1 B
 echo " nermuceq chisht tivy"

  done
}

function dasht
{
  for i in {1..3}
  do
     echo "-------"
     echo "|"${map[($i-1)*3+1]}"|"${map[($i-1)*3+2]}"|"${map[($i-1)*3+3]}"|"
  done
  echo "-------"
}

function stugum 
{
      if  [ ${map[1]} = $1 ] && [ ${map[2]} = $1 ] && [ ${map[3]} = $1 ]  
      then
         clear  
         echo "[Good Game] $2 Wins in $j Step"
         exit
      elif  [ ${map[4]} = $1 ] && [ ${map[5]} = $1 ] && [ ${map[6]} = $1 ]
      then
         clear
         echo "[Good Game] $2 Wins in $j Step"
         exit 
      elif  [ ${map[7]} = $1 ] && [ ${map[8]} = $1 ] && [ ${map[9]} = $1 ]
      then
         clear
         echo "[Good Game] $2 Wins in $j Step"
         exit     
      elif  [ ${map[1]} = $1 ] && [ ${map[4]} = $1 ] && [ ${map[7]} = $1 ]
      then
         clear
         echo "[Good Game] $2 Wins in $j Step"
         exit  
      elif  [ ${map[2]} = $1 ] && [ ${map[5]} = $1 ] && [ ${map[8]} = $1 ]
      then
         clear
         echo "[Good Game] $2 Wins in $j Step"
         exit 
      elif  [ ${map[3]} = $1 ] && [ ${map[6]} = $1 ] && [ ${map[9]} = $1 ]
      then
         clear
         echo "[Good Game] $2 Wins in $j Step"
        exit     
      elif  [ ${map[1]} = $1 ] && [ ${map[5]} = $1 ] && [ ${map[9]} = $1 ]
      then
         clear
         echo "[Good Game] $2 Wins in $j Step"
         exit  
      elif  [ ${map[3]} = $1 ] && [ ${map[5]} = $1 ] && [ ${map[7]} = $1 ]
      then
         clear
         echo "[Good Game] $2 Wins in $j Step"
         exit
      fi
}


clear
echo "*****GAME STARTED*****"
echo "-X- player Name ?"
read name
echo "-O- player Name ?"
read name2
clear

for i in {1..9} 
do
   map[i]=$i
done

for j in {1..9}
do
   
   let pl=$(($j%2)) 
   echo "pl=" $pl
   clear
   if [ $pl -eq 1 ]
   then
      clear
      echo "____________________________________ "
      echo "                                     "      
      echo "Player $name with -X-  $j Step" 
      echo "____________________________________ "
      dasht
      cin      
      map[$B]="X"     
   fi
   if [ $pl -eq 0 ]
   then
      clear
      echo "____________________________________ "
      echo "                                     "
      echo "Player $name2 with -O- $j Step " 
      echo "____________________________________ "
      dasht
      cin
      map[$B]="O"
   fi

   if [ $j -gt 4 ]
   then
      stugum X $name
      stugum O $name2
   fi 
               
   if [ $j = 9 ] 
   then
     clear
     echo "*********************************"  
     echo "            Standoff             "	
     echo "*********************************"
   fi
done