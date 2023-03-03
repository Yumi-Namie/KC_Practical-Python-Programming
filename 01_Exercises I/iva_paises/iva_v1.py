lista_ivas = {
    "hungria": 27,
    "croacia": 25,
    "dinamarca": 25,
    "suecia": 25,
    "finlandia": 24,
    "rumania": 24,
    "grecia": 23,
    "irlanda": 23,
    "polonia": 23, 
    "portugal": 23,
    "eslovenia": 22,
    "italia": 22,
    "españa": 21,
    "belgica": 21,
    "letonia": 21,
    "lituania": 21,
    "paises bajos": 21,
    "republica checa": 21,
    "austria": 20,
    "bulgaria": 20,
    "eslovaquia": 20,
    "estonia": 20,
    "francia": 20,
    "reino unido": 20,
    "alemania": 19,
    "chipre": 19,
    "malta": 18,
    "luxemburgo": 19
}

precio = input("Introduzca un valor: ")
precio = round(float(precio),2)
pais = input("Pais: ")
pais = pais.lower()

if lista_ivas.get(pais):
    iva = precio*lista_ivas[pais]/100
else:
    iva = 0

total = precio + iva

print(f"El IVA {lista_ivas[pais]} de valor de {iva} sobre el precio {precio} es de €{total}")