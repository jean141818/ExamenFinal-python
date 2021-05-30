import os
ruta = os.getcwd()
n = int (input("Ingrese un numero: "))
file = f'\\tabla - {n}.txt'
with open (ruta + file, mode = 'w') as f:
    for i in range(1,12):
        f.write(f'{n} * {i} = {(n*i)} \n')
        
