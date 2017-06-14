#!/bin/bash
mutq ()
{
while [ $B == $ochinyan[$B] ]
do
read -n 1 B
done
}


clear

for i in {1..9} 
do
   ochinyan[i]=$i
done


for i in {1..3}
do
   echo "-------"
   echo "|"${ochinyan[($i-1)*3+1]}"|"${ochinyan[($i-1)*3+2]}"|"${ochinyan[($i-1)*3+3]}"|" 

done

echo "-------"



for j in {1..9}
do
   read -n 1 B
   pl=$(($j%2)) 
   clear
   if [ $pl -eq 1 ]
   then
      ochinyan[$B]="x"
   fi

   if [ $pl -eq 0 ]
   then
      ochinyan[$B]="o"
   fi

   for i in {1..3}
   do
      echo "-------"
      echo "|"${ochinyan[($i-1)*3+1]}"|"${ochinyan[($i-1)*3+2]}"|"${ochinyan[($i-1)*3+3]}"|"
   done
   echo "-------"
done
