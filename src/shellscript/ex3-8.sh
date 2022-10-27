#!/bin/sh

DBASE="DB.txt"

tell_add(){
 echo -n "이름 : "
 read name

 echo -n "전화번호 : "
 read tel

 if [ ! -f $DBASE ];
 then
  touch $DBASE
 fi
 echo $name $tel >> $DBASE
}

tell_add
