def genera_tabla(n):
    
    for i in range (1,11):
        print("{:>2} x {} = {:>2}".format(i, n, i*n))


numero_solicitado = input("Dime un nº para la tabla de multiplicar ")

while True:
    try:
        numero = int(numero_solicitado)
        while numero < 0 : 
            print("Something wrong. Invalid ipunt")
            numero_solicitado = input("Dime un nº para la tabla de multiplicar ")
            numero = int(numero_solicitado)
        break     
    except ValueError:
        print("Something wrong. Invalid ipunt")
        numero_solicitado = input("Dime un nº para la tabla de multiplicar ")
    break
    
    
print("La tabla de", numero, "es:")
genera_tabla(numero)