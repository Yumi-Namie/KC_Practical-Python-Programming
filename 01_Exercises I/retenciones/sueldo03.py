import sueldo03_f

strMisueldo = input("Introduce sueldo: ")
s = float(strMisueldo) #transformar una str en float de nº con decimales


#Búsqueda de limites
irpf = sueldo03_f.buscaRetencion(s)
# Cálculo de pagas
miSueldoNeto = sueldo03_f.netoAnual(s, irpf)

mensual12 = miSueldoNeto/12
mensual14 = miSueldoNeto/14

print("12 pagas de: ", mensual12)
print("14 pagas de: ", mensual14)