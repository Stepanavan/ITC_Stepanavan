#!/bin/bash

for i in `ls -R| grep ^-`
do
echo $i
chmod 777 $i
done