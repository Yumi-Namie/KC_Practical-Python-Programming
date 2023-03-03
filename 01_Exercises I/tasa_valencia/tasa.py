"""
Construye un programa que aplique una tasa a un precio en función de donde se aplique.
Así si la provincia en la que se aplica es 'VA' (Valencia) se debe incrementar el precio en un 5,5%.
En otro caso no se aplicará esta tasa. La salida debe ser distinta en función de la provincia.
"""

#saber la provincia y el precio
str_provincia = input("Cual es la provincia? ")
str_valor = input("Cual es el valor? ")

provincia = str_provincia.lower()
valor = round(float(str_valor),2)
tasa = 0

if provincia == 'valencia':
    tasa = valor * 0.055
    total = valor + tasa

total = valor + tasa

print(f"El total es €{total}")