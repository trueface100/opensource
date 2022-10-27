#!/bin/sh

dir=$1
if [ ! -d $dir ]; then
	mkdir $dir
fi 
eval cd $dir
eval touch file0.txt
eval touch file1.txt
eval touch file2.txt
eval touch file3.txt
eval touch file4.txt
eval tar -cvf files.tar $dir
exit 0
