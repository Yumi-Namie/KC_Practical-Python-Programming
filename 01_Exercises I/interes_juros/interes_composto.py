capital_ini = input("Capital inicial: ")
interes = input ("Interés inicial: ")
time = input ("Tiempo en años: ")
meses = input("Nº de meses qie se acumula el interés: ")

capital = round(float(capital_ini),2)
inter = round(float(interes),2)/100
time = int(time)
m = int(meses)

total = capital*(1 + inter/m)**(time*m)

total = round(float(total),2)

print(f"{capital} invertidos al {inter}% durante {time} años con {m} meses por año se transofrman en {total} ")