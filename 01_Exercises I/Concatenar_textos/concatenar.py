"""
Construir un programa que pida una cita y un autor.
Devolver una única cadena con la cita entre comillas y el autor.
"""

frase = input ("Dime una frase famosa ")
autor = input ("Quien es su autor ")

print("La frase '{}' ({} caract), autor: {} ({} caractokay) ".format(frase, len(frase), autor, len(autor)))