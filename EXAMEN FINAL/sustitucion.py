clave = ''
while len(clave) < 26:
    clave = input ( "Ingrese su clave (26 letras): ")
    if len(clave) < 26:
        print("Incorrecto, tiene que ser de 26 letras")
key = []
for i in clave:
    key.append(i)
                          
import string        
abc = list(string.ascii_lowercase)

plaintext = input("Ingrese palabra: ")
ciphertext = ''
for k in range (len(plaintext)):
    for j,l in enumerate(abc):
        if plaintext[k].lower() == l:
            ciphertext += clave[j]
         
    
print( "plaintext: " + plaintext)
print( "ciphertext: " + ciphertext)

    


