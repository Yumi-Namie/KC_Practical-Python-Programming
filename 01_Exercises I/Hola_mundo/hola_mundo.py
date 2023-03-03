import random

saludo = ["Hey there", "Hello, ", "Hola", "Hi"]

name = input("¿Cómo te llamas?")

nsaludos = random.randint(0,3)

print(saludo[nsaludos], name + "!")

