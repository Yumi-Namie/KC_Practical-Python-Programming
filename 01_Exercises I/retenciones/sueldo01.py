#tuple o array de sueldos, lista de datos 
sueldos = (12450, 20200, 35200, 60000, 70000, 100000,10000000)
retenciones = (1.55, 13.32, 20.08, 26.84, 29.91, 33.94, 44.88)

strMisueldo = input("Introduce sueldo: ")
miSueldo = float(strMisueldo) #transformar una str en float de nº con decimales

puntero = 0
while miSueldo >= sueldos[puntero]:
    puntero = puntero + 1

irpf = retenciones[puntero-1] + ((miSueldo - sueldos[puntero-1])*(retenciones[puntero]-retenciones[puntero-1])/ (sueldos[puntero]-sueldos[puntero-1]))

irpfTotal = irpf + 6.35

miSueldoNeto = miSueldo * (100-irpfTotal)/100

mensual12 = miSueldoNeto/12
mensual14 = miSueldoNeto/14

print("12 pagas de: ", mensual12)
print("14 pagas de: ", mensual14)