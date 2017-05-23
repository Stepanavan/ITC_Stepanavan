#!/bin/bash

for i in {1..20}
do
mkdir lolo$i
cd lolo$i
let k=$i+1
touch lulu$k
done