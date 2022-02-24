#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 23:35:54 2022

@author: paul
"""

import matplotlib.pyplot as plt
import sys, os
import statistics as stats
import numpy as np

arch ="persona.txt"
file= open(arch)
datos = file.readlines()
datos = datos[0]

flag=1
tam=len(datos)
sep=tam
while flag==1:
    esp=datos.find(" ",sep-1)
    if esp>=0:
        ip=datos[esp+1:tam]
        name=datos[0:esp]
        flag=0
    else:
        sep=sep-1
            

dic=[name,ip]
  


arch ="name_ip.txt"
file2= open(arch)
datos2 = file2.readlines()

flag2=0
cont=0


    
for i in datos2:
    fila=eval(i)
    if fila[1]==dic[1]:
        fila[0]=dic[0]
        dic2=[fila[0],fila[1]]    
        datos2[cont]=str(dic2)+"\n"
        flag2=1
    cont=cont+1



if flag2==0:
    file2 = open("name_ip.txt", "a")
    file2.write(str(dic))
    file2.close()
else:
    file2 = open("name_ip.txt", "w")
    file2.write("")
    file2.close()
    tamanos=len(datos2)
    cont2=1
    for j in datos2:    
        file2 = open("name_ip.txt", "a")
        if tamanos==cont2:
            file2.write(str(j))
        elif cont2==1:        
            file2.write(str(j))
        else:
            file2.write(str(j))
        file2.close()
        cont2=cont2+1



        
        
    








