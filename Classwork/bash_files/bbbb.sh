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

let ochinyan[0]=0



echo "player 1"

dasht

j=1

while [ $j -lt 10 ]
do
   read -n 1 B
   let B=$B
   let k=$B-${ochinyan[$B]}
   while [ $k -ne 0 ]
   do
       read -n 1 B
       let B=$B-0
       let k=$B-${ochinyan[$B]}
       let j=$j-1
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
