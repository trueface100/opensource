#!/bin/sh

num=$1
while [ $num -gt 0 ]
do
 echo "hello wolrd"
 num=$(expr $num - 1)
done

