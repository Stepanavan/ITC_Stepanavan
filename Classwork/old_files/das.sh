#!/bin/bash
clear
echo -e "\033[1;37;35m*****GAME STARTED*****\033[0m"
echo -e "\033[1;33;33m-X- player Name ? \033[0m"
read name
echo -e "\033[1;33;33m-O- player Name ? \033[0m"
read name2
clear
cin()
{
while [ !$B ]
do 
   read -n 1 B
if [ $B = ${map[$B]} ] 2> /dev/null
then
   #rm -f /tmp/tmp.txt
   break
elif [ $B != ${map[$B]} ] 2> /dev/null
then 
   #rm -f /tmp/tmp.txt
   let ${map[$B]}=$B 
   continue
fi
done
}

for i in {1..9} 
do
   map[i]=$i
done
clear
echo -e "Press \033[1;34;40mENTER\033[0m For change 1st Player  "
echo "____________________________________ "
echo "                                     "
echo -e "\033[1;33;33m$name\033[0m Play first with \033[1;34;40mX\033[0m"
echo -e "\033[1;33;33m$name2\033[0m Play second with \033[1;34;40mO\033[0m"
echo "                                     "
echo "____________________________________ "
for i in {1..3}
do
   echo -e "\033[1;37;35m-------\033[1m"
   echo -e "\033[1;37;35m|\033[0m"${map[($i-1)*3+1]}"\033[1;37;35m|\033[0m"${map[($i-1)*3+2]}"\033[1;37;35m|\033[0m"${map[($i-1)*3+3]}"\033[1;37;35m|\033[0m"  
done
echo -e "\033[1;37;35m-------\033[0m"
while [ true ]
do
for j in {1..9}
do
   cin    
   let pl=$(($j%2)) 
   clear
   if [ $pl -eq 1 ]
   then
      clear
      echo "____________________________________ "
      echo "                                     "
      echo -e "Player \033[1;33;33m$name2\033[0m with - \033[1;34;40mX\033[0m - $j Step " 
      echo "____________________________________ "
      map[$B]="X"
   fi
   if [ $pl -eq 0 ]
   then
      clear
      echo "____________________________________ "
      echo "                                     "      
      echo -e "Player \033[1;33;33m$name\033[0m with \033[1;34;40mO\033[0m  $j Step" 
      echo "____________________________________ "
      map[$B]="O"   
   fi
   for i in {1..3}
   do
      echo -e "\033[1;37;35m-------\033[0m"
      echo -e "\033[1;37;35m|\033[0m"${map[($i-1)*3+1]}"\033[1;37;35m|\033[0m"${map[($i-1)*3+2]}"\033[1;37;35m|\033[0m"${map[($i-1)*3+3]}"\033[1;37;35m|\033[0m"  
      # player 1 win situations ----------------------------------------------------------------------------------------------------------------------------- 
if  [ ${map[1]} = "X" ] && [ ${map[2]} = "X" ] && [ ${map[3]} = "X" ]  
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit
      elif  [ ${map[4]} = "X" ] && [ ${map[5]} = "X" ] && [ ${map[6]} = "X" ]
      then
         clear
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit   
      elif  [ ${map[7]} = "X" ] && [ ${map[8]} = "X" ] && [ ${map[9]} = "X" ]
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit      
      elif  [ ${map[1]} = "X" ] && [ ${map[4]} = "X" ] && [ ${map[7]} = "X" ]
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit    
      elif  [ ${map[1]} = "X" ] && [ ${map[4]} = "X" ] && [ ${map[7]} = "X" ]
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit     
      elif  [ ${map[1]} = "X" ] && [ ${map[4]} = "X" ] && [ ${map[7]} = "X" ]
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit           
      elif  [ ${map[1]} = "X" ] && [ ${map[4]} = "X" ] && [ ${map[7]} = "X" ]
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit       
      elif  [ ${map[2]} = "X" ] && [ ${map[5]} = "X" ] && [ ${map[8]} = "X" ]
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit    
      elif  [ ${map[3]} = "X" ] && [ ${map[6]} = "X" ] && [ ${map[9]} = "X" ]
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit    
      elif  [ ${map[1]} = "X" ] && [ ${map[5]} = "X" ] && [ ${map[9]} = "X" ]
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit     
      elif  [ ${map[3]} = "X" ] && [ ${map[5]} = "X" ] && [ ${map[7]} = "X" ]
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
      # player 2 win situations --------------------------------------------------------------------------------------------------------------------------
      elif  [ ${map[1]} = "O" ] && [ ${map[2]} = "O" ] && [ ${map[3]} = "O" ]  
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name2 Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit    
      elif  [ ${map[4]} = "O" ] && [ ${map[5]} = "O" ] && [ ${map[6]} = "O" ]
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name2 Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit   
      elif  [ ${map[7]} = "O" ] && [ ${map[8]} = "O" ] && [ ${map[9]} = "O" ]
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name2 Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit    
      elif  [ ${map[1]} = "O" ] && [ ${map[4]} = "O" ] && [ ${map[7]} = "O" ]
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name2 Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit     
      elif  [ ${map[1]} = "O" ] && [ ${map[4]} = "O" ] && [ ${map[7]} = "O" ]
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name2 Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit    
      elif  [ ${map[1]} = "O" ] && [ ${map[4]} = "O" ] && [ ${map[7]} = "O" ]
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name2 Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit         
      elif  [ ${map[1]} = "O" ] && [ ${map[4]} = "O" ] && [ ${map[7]} = "O" ]
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name2 Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit     
      elif  [ ${map[2]} = "O" ] && [ ${map[5]} = "O" ] && [ ${map[8]} = "O" ]
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name2 Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit     
      elif  [ ${map[3]} = "O" ] && [ ${map[6]} = "O" ] && [ ${map[9]} = "O" ]
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name2 Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit   
      elif  [ ${map[1]} = "O" ] && [ ${map[5]} = "O" ] && [ ${map[9]} = "O" ]
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name2 Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit    
      elif  [ ${map[3]} = "O" ] && [ ${map[5]} = "O" ] && [ ${map[7]} = "O" ]
      then
         clear
         echo -e "\033[1;37;35m*********************************\033[0m"
         echo "[Good Game] $name2 Wins in $j Step"
         echo -e "\033[1;37;35m*********************************\033[0m"
         exit
    fi                                    
   done
	   if [ $j = 9 ] 
	   then
	       clear
	       echo -e "\033[1;37;35m*********************************\033[0m"  
	       echo -e "            Standoff            "	
	       echo -e "\033[1;37;35m*********************************\033[0m"
	       exit
	   fi
      echo -e "\033[1;37;35m-------\033[0m"
done
done
clear