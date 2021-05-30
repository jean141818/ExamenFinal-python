def validar (trj):
    s = 0
    for i in range(0,len(trj),2) :
        s = s + int(trj[i]) * 2
        
    s1 = 0
    for i in range(1,len(trj),2):
        s1 = s1 + int(trj[i])
        
    if ( (s + s1) % 10  == 0 ):
        return 0
    else:
        return 1
    
trj = input("Ingrese su N° de Tarjeta: ")

if len(trj) == 13 or len(trj) == 14  and validar (trj):
    if trj[0] == '4':
        print("VISA")
        
elif len(trj)==15 and validar (trj):
    if trj[0] == '4':
        print("VISA")
    else:
        print("AMEX")

elif len(trj) == 16 and validar (trj):
    if trj[0] == '4':
        print("VISA")
    else:
        print("MASTERCAD")
    
else:
    print("NO VALIDO")        