#!/bin/bash

liczba_a="5"
echo "uruchomiles skrypt z parametrem o wartosci $1"

if [ $1 -gt $liczba_a ] ; then
    echo "parametr z ktorym skrypt zostal uruchomiony jest wiekszy niz $liczba_a"
else
    echo "mniejsze"
fi