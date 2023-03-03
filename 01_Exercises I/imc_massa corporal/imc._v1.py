
def numerico(entrada, error):
    while True:
        str_valor = input(entrada)
        try:
            str_valor = float(str_valor)
            break
        except:
            print(error)
            str_valor = input(entrada)
            break
    return float(str_valor)    

peso = numerico("Peso: ","Error, solo digitos numericos")
altura = numerico("Altura: ","Error, solo digitos numéricos" )

imc = peso/altura**2
imc=round(imc,2)


if imc < 16:
    clas = "Delgadez severa"
elif  imc >= 16 and imc <= 16.99:
    clas = "Delgadez moderada"
elif imc >= 17 and imc <= 18.49:
    clas = "Delgadez leve"
elif imc >= 18.50 and imc <= 25:
    clas = "Normal"
elif imc >= 25.01 and imc<= 29.99:
    clas="Preobeso"
elif imc >= 30 and imc <=34.99:
    clas="Obesidade leve"
elif imc >= 35 and imc <=34.99:
    clas = "Obesidade media"
else:
    clas="Obesidade morbida"


print(f"Tu IMC es {imc} - considerado clasificación: {clas}")


