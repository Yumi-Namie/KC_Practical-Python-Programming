mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ"
numeros= "012345689"

def myLower(cadena):
    res = ""
    for caracter in cadena:
        if caracter in mayusculas:
            res += chr(ord(caracter)+32) 
        else:
            if caracter in numeros:
                print("Invalid")
                res = ""
                break
            else:
                res += caracter
        
    return res   
    


cadena = input("dime algo: ")
print(myLower(cadena))

