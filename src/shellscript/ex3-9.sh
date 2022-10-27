#!/bin/sh

ans= $1
while read line
do
 case $line in
  $ans )
    echo"$line";;
  *)
   ;;
 esac
done < DB.txt

