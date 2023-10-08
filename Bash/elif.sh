#!/bin/bash

command1=`netstat -tulpn | grep 0.0.0.0 | awk '{print $4 $6}' | grep LISTEN`
echo $command1 > $1
command2=`cat $1`

echo $command2


#UWAGA: nie dziala
if [ $command1 -eq $command2 ] ; then
    echo "zgadza sie"
else
    echo "nie zgadza sie"
# elif [ $command1 -eq $command2 ] ; then
#     echo "to tez sie zgadza"
fi
