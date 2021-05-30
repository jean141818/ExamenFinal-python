import pandas as pd

dicx= {
    "nombre": ["Rick", "Morty"],
    "apellido": ["Sanchez", "Smith"],
    "edad": [60, 14]
    }
rick_morty = pd.DataFrame(dicx)

print(rick_morty) 