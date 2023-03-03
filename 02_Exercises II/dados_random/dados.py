from random import randint

#Suma de valores de los dados: minimo 1+1=2 y el máximo 6+6=12
dices = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
#datos fornecidos para comparar con el resultado simulado:
frecuency_expected = {2:2.78, 3:5.56, 4:8.33, 5:11.11, 6:13.89, 7:16.67, 8:13.89, 9:11.11, 10:8.33, 11:5.56, 12:2.78}  
#cantidad de veces a tirar los dados:
numb_total_rolls = 1000


def roll_dices():
    return randint(1,6) + randint(1,6)

#en un rango de 0 a 1000 contar frecuencias
for _ in range (1,numb_total_rolls +1):
    roll = roll_dices( )
    #añadir valor para cada puntos del dado en el dicionario:
    dices[roll] +=1

print("Total\tSimulated\tExpected")
print("\t  Percent\t Percent")

for i in dices:
    print("{:2d}\t{:>9.2f}\t{:>8}".format(i, dices[i]/10, frecuency_expected[i]))



