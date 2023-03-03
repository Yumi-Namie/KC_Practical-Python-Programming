product1 = input("Precio del producto 1: ")
product2 = input("Precio del producto 2: ")
product3 = input("Precio del producto 3: ")

while True:
    try:
        p1 = float(product1)
        p2 = float(product2)
        p3 = float(product3)

        if p1 < 0 or p2 <0 or p3<0:
            print("opps...solo nº positivos")
            product1 = input("Precio del producto 1: ")
            product2 = input("Precio del producto 2: ")
            product3 = input("Precio del producto 3: ")
        else:
            break
    except ValueError:
        print("No se aceptan textos")
        product1 = input("Precio del producto 1: ")
        product2 = input("Precio del producto 2: ")
        product3 = input("Precio del producto 3: ")

subtotal = 0
subtotal += p1
subtotal += p2
subtotal += p3

tasa = 1.055
tasa_total = tasa*subtotal
valor_total= subtotal + tasa_total

print("Productos: Item1: {} Item2: {} Item3: {}".format(p1,p2,p3))
print("Subtotal: {}".format(subtotal))
print("Valor de 5,5%. sobre los productos: {}".format(tasa_total))
print("Valor total a pagar: €{} ".format(valor_total))
