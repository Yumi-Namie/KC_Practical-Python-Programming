"""
Entrada solamente numerica y no textos
numeros distintos, o sea, no duplicados
cantidad - tantos numeros como el usuario quiera
econtrar el nº mayor sin el 'max'.: max(lista)
"""


#crear funcion para entrada solamente numericos
def input_numerico (msg, error):
    while True:
        str_number = input(msg)

        try:
            number = float(str_number)
            break
        except:
            print(error)
    return number

#crear variables
lista = []
mayor = 0
menor = 0

#preguntar cuantos nº a inserir
cantidad = int(input_numerico("Cantidad de numeros a inserir: ", "invalid"))


while (cantidad >0):
    n = input_numerico("Dime un nº ", "Invalid input: its not a number")
    
    if n in lista: #no quiero numeros duplicados
        False
        print("Error")
    else: 
        lista.append(n)
        cantidad = cantidad -1

#Recoger y comparar        
mayor = lista[0]
menor = lista[0]
for n in lista:
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n

    

#imprimir resultado
print("Lista: ", lista)
print("Mayor nº ", mayor)
print("Menor nº: ", menor)
