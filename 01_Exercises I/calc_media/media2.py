def num_float(msg, error):
    
    while True:
        try:
            str_nota = input(msg)
            nota = float(str_nota)
            break  
        except:
            print(error)
    return nota

nota_total=0
contador = 0

while True:

    nota = num_float("Introduce una nota ", "Invalid input")
    nota_total = nota_total + nota
    
    if nota == 0 and contador == 0:
        print("error")
    if nota == 0 and contador !=0:
        break
    contador = contador + 1
    
media = nota_total / contador

print(media)