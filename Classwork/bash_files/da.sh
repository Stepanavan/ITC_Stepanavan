#!/bin/bash 

cd
cd Desktop

i=0
while  [ $i -lt 20 ] || [ $i -eq 20 ]  
do
   mkdir "astghik$i"
   cd "astghik$i"
   let b=$i+1
   if [ $b -gt 5 ]
   then
     touch   "ala$b"
   fi
   let i=$i+1
done
                

