"""
1- Cada persona puede coger solo un unico trozo por pizza.
2- Las pizzas solo pueden ser cortadas en números pares.
"""
#funcion para entrada de numeros entero y positivo

def num_entero_posit(entrada, error):
 
    numero = input(entrada)

    while True:
        try:
            numero = int(numero)

            if numero < 0:
                print(error)
                numero = input(entrada)
            else:   
                break
        except ValueError:
            print(error)
            numero = input(entrada)
    return numero
  

personas = num_entero_posit("Número de personas ?", "Error, introduzca una cifra entera positiva")
pizzas = num_entero_posit("Número de pizzas? ", "Error, introduzca una cifra entera y positiva")

if personas %2 == 0: #si es PAR
    coge = pizzas
    sobra = 0
else:
    coge = pizzas
    sobra = pizzas

#variables plural / singular
str_personas = 'persona'
str_pizza = 'pizza'
str_pieza = 'pieza'
str_sobra = 'sobra'

if pizzas >1:
    str_pizza += 's'
    str_sobra += 'n'
    str_pieza += 's'
if personas >1:
    str_personas += 's'

print(f"Para compartir {pizzas} {str_pizza} en {personas} {str_personas}")
print(f"Cada persona coge {coge} {str_pieza}")
print(f"{str_sobra}: {sobra}")


