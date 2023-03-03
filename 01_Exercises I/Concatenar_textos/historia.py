plantilla = "Un 0 1 debe 2 3"

nombre = input("Dime un nombre... ")
verbo = input("Dime un verbo... ")
adverbio = input("Dime un adverbio... ")
adjetivo = input("Dime un adjetivo... ")

ix = 0
frase = ""

while ix < len(plantilla):
  car = plantilla[ix]
  
  if car == "0":
    frase = frase + nombre
  elif car == "1":
    frase = frase + adjetivo
  elif car == "2":
    frase = frase + verbo
  elif car == "3":
    frase = frase + adverbio
  else:
    frase = frase + car
    
  ix = ix + 1

  
print(frase)