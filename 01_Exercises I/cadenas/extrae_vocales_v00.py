palabra= input("Diga una palabra")

vocales = ""
for caracter in palabra:
    if caracter =="a" or caracter =="e" or caracter =="i" or caracter=="o" or caracter =="u":
        vocales += caracter

print("los vocales de ", palabra, "son", vocales)
    