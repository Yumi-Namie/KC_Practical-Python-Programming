#def validPwd():

letra = ("ABCDEFGHIJKLMNOPQWXYZabcdefghijklmnopqrstuvwxwz")
letra = list(letra)
number = list(range(0,10))

pwd = input("Pasword: ")
pwd = list(pwd)

ctde = 0
ctde_letra = 0
ctde_number = 0

#Comprobar si es mayor o menor que 8 caracteres:
for n in pwd:
    ctde = ctde + 1


if ctde < 8: #comprabar si es  solo numero
    try:
        for n in pwd:
            n = int(n)
        print("Muy debil")
    except:
        print("Débil")

if ctde >= 8:
    
    for i in pwd:
        try:
            i = int(i)
            if i in number:
                ctde_number = ctde_number +1
            else:
                pass
        except:
            if i in letra:
                ctde_letra = ctde_letra +1
                
            else:
                pass
    
    if ctde_letra + ctde_number == ctde:
        print("Fuerte")
    else:
        print("Muy fuerte")




















   


    

        
    




