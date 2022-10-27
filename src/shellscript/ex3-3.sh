#!/bin/sh

w=$1
h=$2
h_m=$( echo "scale=1; $h / 100" |bc )
BMI=$( echo "scale=1; $w / $h_m / $h_m " |bc )
if [ 'echo "$BMI < 18.5" |bc' -eq 1 ]
then
	echo "저체중입니다." 
else
	if [ 'echo "$BMI > 23" |bc' -eq 1 ]
	then
		echo "과체중입니다."
	else
		echo "정상체중입니다."
	fi
fi
exit 0
