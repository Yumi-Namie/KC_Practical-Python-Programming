texto = input("Dime algo ")
txt = texto
contador = 0

while texto == "":
    print("Error")
    texto = input("Dime algo ")


while texto != "":
    texto = texto[1: ]
    contador +=1
   
print("En '{}' tiene {} caracteres".format(txt, contador))


