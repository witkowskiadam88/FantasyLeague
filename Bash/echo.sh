#!/bin/bash

echo "1" "printowanie skryptu"
echo "2" "$HOME"
echo "3" $HOME    #mozna drukowac z "" oraz bez 
echo "4" \$HOME   #wydrukuje napis $HOME (maskowanie)
echo "5" '$HOME'  #wydrukuje napis $HOME (maskowanie)
echo "6" `pwd`    #zmienna srodowiskowa musi byc zapisana odwrotnym apostrofem
echo "7" pwd      #wydrukuje tylko napis
echo "8" "pwd"    #wydrukuje tylko napis
echo "9" `ls -la`
