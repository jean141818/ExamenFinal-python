def Conv (cad,k):
    newcad = ''
    for i in cad:
        if i.isalpha(): 
            if i.isupper():
                newcad += chr(((ord(i)- 65 + k) % 26)+65)
            else:
                newcad += chr(((ord(i)- 97 + k) % 26)+97)
        else:
            newcad += i
    return newcad
        
        
        
    
cad = input("Ingrese una palabra: ")
k = int (input( "Ingrese clave: "))
print(Conv(cad,k))
