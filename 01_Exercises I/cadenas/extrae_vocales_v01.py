palabra= input("Dime una palabra")

lvocales = ['a', 'e', 'i','o','u','A','E','I','O','U']

def extraer_vocales():
    vocales = ""
    for caracter in palabra:
        if caracter in lvocales:
            vocales += caracter
    return vocales

if lvocales != "":
    print("Los vocales encontrados de", palabra, ":", extraer_vocales())
else:
    print("No hemos encontrado vocales en ", palabra)




"""
if extraer_vocales() != "":
    print("Los vocales encontrados de", palabra, ":", extraer_vocales())
else:
    print("No hemos encontrado vocales en ", palabra)
"""
    
