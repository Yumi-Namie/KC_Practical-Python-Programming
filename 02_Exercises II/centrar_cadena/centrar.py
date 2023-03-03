
text = input("Texto ")
ancho = int(input("Ancho: "))


def centralizer (text, ancho):
    total_space = (ancho - len(text))//2
    result = total_space * " " + text
    return result

print(centralizer(text,ancho))





