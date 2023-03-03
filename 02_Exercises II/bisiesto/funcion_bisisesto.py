#Años bisisestos: 2012,2016,2020,2024,2028,2032,2036,2040...
"""
def es_bisiesto(anyo):
    if anyo % 400 == 0:
        True
    elif anyo % 100 == 0:
        False
    elif anyo % 4 == 0:
        True
    else:
        False
    return es_bisiesto

"""
def es_bisiesto(y):
  return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)


if __name__ == "__main__":
    anyo = int(input("Dime un año: "))
    if es_bisiesto == True:
        print(f"El año {anyo} es bisisesto")
    else:
        print(f"El año {anyo} NO es bisisesto")


