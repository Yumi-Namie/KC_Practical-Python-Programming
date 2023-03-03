dolar = input("Cuantos dolares quieres cambiar: ")
tasa = input("A cuanto la tasa de cambio? ")

do = round(float(dolar),2)
ts = round(float(tasa),2)
total = round(do * ts,2)


input(f"{do} dolares a una tasa de cambio de {ts}\nTotal de €{total}")
