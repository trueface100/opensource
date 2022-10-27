#!/bin/sh

num1=$1
opt=$2
num2=$3
if [ "$opt" = "+" ]
then
 num3=$(expr $num1 + $num2)
elif [ "$opt" = "-" ]
then
 num3=$(expr $num1 - $num2)
elif [ "$opt" = "*" ]
then
 num3=$(expr $num1 \* $num2)
elif [ "$opt" = "/" ]
then
 num3=$(expr $num1 / $num2) 
fi
echo $num3 
