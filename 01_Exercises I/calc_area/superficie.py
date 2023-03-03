
ancho = input ("Dime el ancho ")
largo = input ("Dime el largo ")


while True:
    try:
        ancho = float(ancho)
        largo = float(largo)

        if ancho != float(ancho) and largo !=float(largo):
            print("Error. Vuelva a intentar")
            ancho = input ("Dime el ancho ")
            largo = input ("Dime el largo ")
        else:
            break
    except ValueError:
        print("Se aceptan solo números")
        ancho = input ("Dime el ancho ")
        largo = input ("Dime el largo ")

        
sup_mt = ancho * largo
sup_yd = sup_mt / 0.9144 ** 2

print(f"Superficie en metros cuadrados: {sup_mt} y" f"Superficie en yardas cuadradas: {sup_yd}")



