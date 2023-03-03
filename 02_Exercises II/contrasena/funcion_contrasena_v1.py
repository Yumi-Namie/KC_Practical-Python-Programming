def validPwd(passw):

    letras_total = ("ABCDEFGHIJKLMNOPQWXYZabcdefghijklmnopqrstuvwxwz")
    letra = list(letras_total)
    number = list(range(0,10))

    ctde = 0
    ctde_letra = 0
    ctde_number = 0

    #Descobrir length del password: si la suma de nº + letras == len(pwd), no hay caracteres especiales
    pwd = list(passw)
    for n in pwd:
        ctde = ctde + 1

    if ctde < 8: 
        try:
            for n in pwd:
                n = int(n) #comprabar si es  solo numero
            print("Muy debil")
        except:
            print("Débil")

    if ctde >= 8:
        for i in pwd:
            try:
                i = int(i)
                if i in number:
                    ctde_number = ctde_number +1 #descobrir ctde de numeros
            except:
                if i in letra:
                    ctde_letra = ctde_letra +1 #descobrir ctde de letras
        
        if ctde_letra + ctde_number == ctde:
            print("Fuerte")
        else:
            print("Muy fuerte") #si la suma de nº + letras != len(pwd), hay caracteres especiales




















   


    

        
    




