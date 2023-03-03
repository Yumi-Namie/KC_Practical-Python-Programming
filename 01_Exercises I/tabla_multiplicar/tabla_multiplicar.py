numero_solicitado = int(input("Dime un nº para la tabla de multiplicar"))



def genera_tabla(n):
    
    for i in range (1,11):
        print("{:>2} x {} = {:>2}".format(i, n, i*n))
    
    
print("La tabla de", numero_solicitado, "es:")
genera_tabla(numero_solicitado)