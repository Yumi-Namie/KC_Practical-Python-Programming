texto = input("Dime algo")
caracteres = len(texto)


while caracteres <= 0:
    print("No has escrito nada. Intentalo de nuevo")
    texto = input("Dime una palabra o frase")
    caracteres = len(texto)
    

print("En '{}' hay {} caracteres".format(texto,caracteres))









