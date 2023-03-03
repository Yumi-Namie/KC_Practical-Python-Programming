def contarCaracteres(texto):
    return len(texto)

def contarPalabras(texto):
    return len(texto.split())

def contarVocales(texto):
    vocales = 0
    for i in texto:
        if i in "AEIOUaeiou":
            vocales +=1
    return vocales
            
def contarConsonantes(texto):
    consoantes = 0
    for letra in texto:
        if letra in "bcdfghjklmnñpqrstuvwxyzBCDFGHJKLMNÑPQRSTUVWXYZ":
            consoantes +=1
    return consoantes

if __name__ == '__main__':
    texto = input("Dime algo ")

    #Printar de forma de tabla tabulada

    print('Caracteres.: {:4d}'.format(contarCaracteres(texto)))
    print('Palabras...: {:4d}'.format(contarPalabras(texto)))
    print('Vocales....: {:4d}'.format(contarVocales(texto)))
    print('Consonates.: {:4d}'.format(contarConsonantes(texto)))


    """
    https://www.delftstack.com/pt/howto/python/python-count-words-in-string/
    """