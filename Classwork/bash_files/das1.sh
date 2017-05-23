
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
     echo "|"${map[($i*3)-2]}"|"${map[($i*3)-1]}"|"${map[($i*3)]}"|"
  done
  echo "-------"
}

function stugum
{
for i in {1..3}
do
      if [ ${map[($i*3)-2]} = $1 ] && [ ${map[($i*3)-1]} = $1 ] && [ ${map[($i*3)]} = $1 ]
      then
         clear  
         echo "[Good Game] $2 Wins in $j Step"
         exit
      elif [ ${map[$i]} = $1 ] && [ ${map[$i+3]} = $1 ] && [ ${map[$i+6]} = $1 ]
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
done
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
