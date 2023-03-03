
ancho = input("Dime el ancho en metros de la pared: ")
largo = input("Dime el largo en metros de la pared: ")

a = int(ancho)
l = int(largo)
area = a * l
litros = (5*area)/100
botes = litros //5

#if ternario
botes += 1  if litros %5 >0 else 0
    

print("Necesitarás {} litros para pintar {} metros cuadrados de techo.".format(litros,area))
print("Deberás comprar {} botes de 5L de tinta".format(botes))

