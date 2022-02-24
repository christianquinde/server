#!/bin/bash

FICHERO=/media/christian/CPQR/Tesis/App_Video/server/cliente.txt

var=0
elim=0

while [[ var==10000 ]]; do
   if [ -f $FICHERO ]
   then
      echo "El fichero existe"
      ip=$(cat cliente.txt)
      echo $ip 
      nc -w 2 $ip 7777 < name_ip.txt
      nc -w 2 $ip 7777 < name_ip.txt
      nc -w 2 $ip 7777 < name_ip.txt
      rm cliente.txt
   else
      echo "El fichero no existe"
      chmod 777 cliente.txt
      netcat -l 8888 | pv > cliente.txt
   fi 

sleep 1
var=$var+1

done
