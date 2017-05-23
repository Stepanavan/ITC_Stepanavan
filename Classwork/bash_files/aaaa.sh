#!/bin/bash
dasht()
{
for i in {1..3}
do
   echo "-------"
   echo "|"${ochinyan[($i-1)*3+1]}"|"${ochinyan[($i-1)*3+2]}"|"${ochinyan[($i-1)*3+3]}"|" 

done
echo "-------"
}

reset

for i in {1..9} 
do
   ochinyan[i]=$i
done

ochinyan[0]=0



echo "player 1"

dasht

j=1
B=0

while [ $j -lt 10 ]
do
   echo ${ochinyan[$B]} 
   until [ $B -eq ${ochinyan[$B]} ]
   do
       read -n 1 B
       let B=$B-0
       let j=$j-1
       echo $j
       clear
   done
   pl=$(($j%2)) 
   clear

   if [ $pl -eq 1 ]
   then
      ochinyan[$B]="x"
      echo "player 2"
   fi

   if [ $pl -eq 0 ]
   then
      echo "player 1"
      ochinyan[$B]="o"
   fi
   dasht
   (( j++ ))
done
