mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"

def myLower(cadena):
    res = ""
    for caracter in cadena:
        if caracter in mayusculas:
            res += chr(ord(caracter)+32)
        else:
            res += caracter
    return res


# Cada letra, o sea, cada caracter é representado por un nº y se diferencian entre mayusculas y minusculas.
# Si 'a'es 97 y 'A' es 65... la diferencia entre ellos  es de 32 (ver la tabla ASCII)
# En la solucion, si la letra de la cadena es mayuscula, la transformamos en numero y despues la transformamos en su codigo em minuscula añadindo 32.
# Si no, añadimos en el resultado tal cual como está





