def comp (datos,line):
    sumas = []
    for i in datos:
        l = line.count(i)
        sumas.append(l)
    
    return sumas            

import os
ruta = os.getcwd()
file = '\\databases\\large.csv'
file2 = '\\sequences\\5.txt'

with open (ruta + file2 , 'r') as f:
    line = f.read()
      
with open (ruta + file, 'r') as arch:
    lista = [linea.rstrip() for linea in arch]
    datos = lista.pop(0)
    datos = datos.split(',')
    datos.pop(0)
    sumas = comp(datos,line)
    for i in lista:
        lista2 = i.split(',')
        nombre = lista2.pop(0)
        lista2.pop(0)
        if sumas == lista2:
            print(nombre)

        
               

