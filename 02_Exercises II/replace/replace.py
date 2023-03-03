cadena = input("Palabra: ")
posicion = int(input("Posición: "))
nuevoValor = input("Valor: ")

def myReplace(cadena, posicion, nuevoValor):
    txt = list(cadena)
    position = posicion - 1
    txt[position] = nuevoValor
    return txt

texto = myReplace(cadena, posicion, nuevoValor)
print(texto)