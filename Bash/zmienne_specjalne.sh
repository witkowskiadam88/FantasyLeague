#!/bin/bash

echo "skrypt zostal wywoalny przez zmienna specjalna $_"    #zmienna specjalna to zmienna tylko do odczytu

echo "skrypt zostal wywoalny z parametrami przekazanym do skryptu: $1 i $2"

echo "liczba parametrow przekazanych do skryptu to $#"

echo "skrypt uruchomiono z parametrami $@"

echo skrypt uruchomiono z parametrami $@   # "" - nie jest konieczny

echo "PID procesu bierzacej powloki to $$"