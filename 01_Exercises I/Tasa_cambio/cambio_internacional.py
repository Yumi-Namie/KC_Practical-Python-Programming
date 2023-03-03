
cambios = dict(real=.56, yen=0.89, dolar=.93)

moneda = input("Por favor, quieres el cambio de Euros para real, yen o dolar? ")

euros = input("Cuantos euros quieres cambiar: ")

euros = round(float(euros),2)


moneda = moneda.lower()


tasa = cambios.get(moneda)

total = euros * tasa
total = round(float(total),2)

print(f"{euros} € en un valor de {total} {moneda} de una tasa de {tasa}")
















