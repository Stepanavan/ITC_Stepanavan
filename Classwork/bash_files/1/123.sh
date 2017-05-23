#!/bin/bash
again=yes #присваиваем значение "yes" переменной again
while [ "$again" = "yes" ] #Будем выполнять цикл, пока $again будет равно "yes"
do
echo "Please enter a name:"
read name
echo "The name you entered is $name"

echo "Do you wish to continue?"
read again
done
echo "Bye-Bye"
