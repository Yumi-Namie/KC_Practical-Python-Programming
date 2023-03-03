
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
    return str_valor
    

peso = numerico("Peso: ","Error, solo digitos numericos")
altura = numerico("Altura: ","Error, solo digitos numéricos" )

imc = peso/altura**2
imc=round(imc,2)

print(f"Tu IMC es {imc}")
if imc < 18.50:
    print("Estas muy delgado, quizás deberías visitar a tu médico.")
elif imc > 25:
  print("Tienes sobrepeso, quizás deberías visitar a tu médico.")
else:
  print("Estas en tu peso ideal")
