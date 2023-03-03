#Crear funcion para transformar int (n bebidas y volumen)
#crear funcion para  trasnformar float (grado alcoholico)
#Preguntar nº de bebidas, volumen, grado
#una operacion para sumar todo +=

def txt_entero(msg):
    texto = ""
    texto = input(msg)
    texto = int(texto)
    return texto

def txt_float(msg):
    texto = ""
    texto = input(msg)
    texto = float(texto)
    return texto

total_alcohol = 0
mas_bebidas = "S"



while mas_bebidas == "S":
    try:
        bebidas = txt_entero("Nº de bebidas: ")
        volumen = txt_entero("Volumen por bebida: ")
        grado = txt_float("Grado alcohólico: ")
    except ValueError:
        print("Por favor, digite números")
        continue

    total_alcohol += (bebidas * volumen * grado* 0.8) /100 #calculo

    mas_bebidas = input("Otras bebidas? (S / N) ")
    mas_bebidas = mas_bebidas.upper()

ube = total_alcohol/10
ai = ube*0.3

horas = input("Horas transcorridas: ")
horas = int(horas)
alcohol_real = ai - 0.15*horas

print("Alcohol en el sangre: ", alcohol_real)

if alcohol_real < 0.5:
    print("Usted puede conducir")
else:
    print("El máximo permitido es 0.5 g/l.\nUsted no puede conducir")