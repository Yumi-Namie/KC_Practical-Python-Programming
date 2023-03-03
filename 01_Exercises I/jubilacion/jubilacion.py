edad = input("Cuantos años tienes? ")
edad_jubi = input("A qué edad te jubilarás? ")

edad = int(edad)
edad_jubi = int(edad_jubi)

calculo = edad_jubi - edad
ano = 2022 + calculo


if calculo <= 0:
    print("Ya puedes jubilarse")
else:
    print("Te quedan", calculo, "años para jubilarte")
    print("Estamos en 2022, te jubilarás en ", ano)