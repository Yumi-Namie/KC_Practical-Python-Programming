
precio = input("Introduzca un valor: ")
precio = round(float(precio),2)
pais = input("Pais: ")
pais = pais.upper()

if pais == "HUNGRIA":
    iva = 27
elif pais == "CROACIA" or pais == 'DINAMARCA' or pais == "SUECIA":
    iva = 25
elif pais == "FINLANDIA" or pais == "RUMANIA":
    iva = 24
elif pais == "GRECIA" or pais == "IRLANDA" or pais == "POLONIA" or pais =="PORTUGAL":
    iva = 23
elif pais == "ESLOVENIA" or pais == "ITALIA":
    iva = 22

iva = round(float(iva),2)
valor_iva = precio * (iva/100)
total = precio + valor_iva

print(f"El IVA {iva} de valor de  {valor_iva} sobre el precio {precio} es de  €{total}")

