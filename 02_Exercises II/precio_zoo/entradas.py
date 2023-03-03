entrada_baby = 0
entrada_menores = 0
entrada_jubilados = 0
entrada_adultos = 0
edad = ""
cant_baby = 0
cant_menores = 0
cant_adultos = 0
cant_jubi = 0
total_baby = 0
total_menores = 0
total_adultos = 0
total_jubi = 0
n = 1

while edad != 0:
    
    edad = int(input (f"Edad de la persona {n} "))
    n = n + 1
    

    if edad <= 2:
        entrada_baby = 0
        cant_baby +=1 
        total_baby = cant_baby*entrada_baby
    elif edad > 2 and edad <=14:
        entrada_menores = 14
        cant_menores +=1
        total_menores = cant_menores*entrada_menores
    elif edad <= 65:
        entrada_jubilados = 18
        cant_jubi +=1
        total_jubi = cant_jubi*entrada_jubilados
    else:
        entrada_adultos = 23
        cant_adultos +=1
        total_adultos = cant_adultos*entrada_adultos
   
print (f"{cant_baby}x entradas baby (0€): {total_baby:11.2f}€")
print (f"{cant_menores}x entradas menores (14€): {total_menores:>7.2f}€")
print (f"{cant_jubi}x entradas jubilados (18€): {total_jubi:>5.2f}€")
print (f"{cant_adultos}x entradas adultos (23€): {total_adultos:>7.2f}€")
print(f"{'-------':>35}")
print("Valor total: {:>21.2f}€".format( total_baby + total_menores + total_adultos + total_jubi))
