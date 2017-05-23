#!/bin/bash
reset

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

