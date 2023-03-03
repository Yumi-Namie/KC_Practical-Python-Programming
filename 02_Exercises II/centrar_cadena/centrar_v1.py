text = input("Texto ")
ancho = input("Ancho: ")

def centralizer (text, ancho):
    retorno = ""
    try:
        ancho = int(ancho)
        if isinstance(text,str)== True and isinstance(ancho,int) == True:
            total_space = (ancho - len(text))//2
            result = total_space * " " + text
            retorno = result
    except:
        print("Invalid Parameters")
    return retorno
  

print(centralizer(text,ancho))




