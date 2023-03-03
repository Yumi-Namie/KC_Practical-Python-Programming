""""
El cero no se debe incluir en el cálculo de la media
Si el primer valor introducido es un cero el programa mostrará un mensaje de error
Mantener separadas la entrada, salida y proceso dentro del programa.
Si el valor introducido no es numérico volver a pedirlo
"""
#Crear funcion para nº flotantes
def num_float(msg, error):
    
    while True:
        str_nota = input(msg)
        
        try:
            number = float(str_nota)
            print(number)

            while number > 0:
                
                nota_total = nota_total + number 
                contador = contador + 1
        
            return nota_total 
             
        except:
            print(error)
        


nota_total = 0

nota = num_float("Introduce un valor: ", "Error")



media = nota_total

print(media)
