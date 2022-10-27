#!/bin/sh

w=$1
h=$2
BMI= ($w / ( $h * $h ))|bc
if [ $BMI -lt $18.5 ]
then
 echo "저체중입니다." 
elif [ $BMI -ge 18.5 ] && [ $BMI -lt 23 ]
then
 echo "정상체중입니다."
elif [ $BMI -ge 23 ]
then
 echo "과체중입니다."
fi
