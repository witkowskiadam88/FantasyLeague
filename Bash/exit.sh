#!/bin/bash

read -p "wprowadz liczbe:" x

if [ $x -eq 10 ] ; then
echo "przed exitem"
exit 0
echo "po exicie"
else
echo "nie jest rowna 10"
fi