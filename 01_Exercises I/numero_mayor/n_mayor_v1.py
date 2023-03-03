def numerico (msg, error):
    while True:
        str_number = input(msg)

        try:
            number = float(str_number)
            break
        except:
            print(error)
    return number


lista = []

mayor = 0
menor = 0


cantidad = int(input("Cantidad de numeros a inserir: "))

while (cantidad >0):
    n = numerico("Dime un nº ", "Invalid input: its not a number")
    
    if n in lista:
        False
        print("Error")
    else: 
        lista.append(n)
        cantidad = cantidad -1
        


mayor = max(lista)
menor = min(lista)

"""
mayor = lista[0]
for n in lista:
    if n > mayor:
        mayor = n
"""





print("Lista: ", lista)
print("Mayor nº ", mayor)
print("Menor nº: ", menor)
