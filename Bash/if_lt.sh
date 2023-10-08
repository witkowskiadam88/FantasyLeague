#!/bin/bash

free_cpu=`free -m | awk '{print $4}' | sed '2!d'`
echo "$free_cpu"

limit="100"
echo "$limit"

echo "limit to $limit a free_cpu to $free_cpu"

if [ $free_cpu -lt $limit ] ; then
echo "uwaga, pamieci ram jest mniej 100MB "
else
echo "pamięci jest więcej niż 100MB"
fi



