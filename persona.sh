#!/bin/bash

FICHERO=/media/christian/CPQR/Tesis/App_Video/server/persona.txt

var=0
elim=0

while [[ var==10000 ]]; do
   if [ -f $FICHERO ]
   then
      echo "El fichero existe"
      python3 listar.py
      elim=$elim+1
      if [[ elim==20 ]]; then
         rm persona.txt
         elim=0
      fi

   else
      echo "El fichero no existe"
      chmod 777 persona.txt
      netcat -l 8899 | pv > persona.txt
      chmod 777 persona.txt
   fi 

sleep 1
var=$var+1

done

