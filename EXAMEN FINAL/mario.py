n = -1
while n < 0 or  n > 8 :
    n = int (input ("Ingrese un numero: "))
    if n < 0 or  n > 8:
        print( "Numero incorrecto, vuelva a ingresar otro numero...")
        

for i in range(1,n+1): 
    print(' ' * (n-i) + '#' * (i))   
