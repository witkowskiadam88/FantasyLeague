#!/bin/bash

read -p "wprowadz miesiac:" miesiac
echo wprowadziles $miesiac


case $miesiac in
    "Styczen") echo "wprowadziles dobry miesiac, bo jest to $miesiac" ;;
    "Luty") echo "wprowadziles dobry miesiac, bo jest to $miesiac" ;;
    "Marzec") echo "wprowadziles dobry miesiac, bo jest to $miesiac" ;;
    "Kwiecien") echo "wprowadziles dobry miesiac, bo jest to $miesiac" ;;
    "Maj") echo "wprowadziles dobry miesiac, bo jest to $miesiac" ;;
    "Czerwiec") echo "wprowadziles dobry miesiac, bo jest to $miesiac" ;;
    "Lipiec") echo "wprowadziles dobry miesiac, bo jest to $miesiac" ;;
    "Sierpien") echo "wprowadziles dobry miesiac, bo jest to $miesiac" ;;
    "Wrzesien") echo "wprowadziles dobry miesiac, bo jest to $miesiac" ;;
    "Pazdziernik") echo "wprowadziles dobry miesiac, bo jest to $miesiac" ;;
    "Listopad") echo "wprowadziles dobry miesiac, bo jest to $miesiac" ;;
    "Grudzien") echo "wprowadziles dobry miesiac, bo jest to $miesiac" ;;
    *) 
esac

