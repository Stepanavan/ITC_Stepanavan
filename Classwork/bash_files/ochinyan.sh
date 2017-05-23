#!/bin/bash
clear
cd
read j
i=1

until [ $i -eq $j ]
do
  mkdir "astghik$i"
  cd "astghik$i"
  let i=$i+1
done