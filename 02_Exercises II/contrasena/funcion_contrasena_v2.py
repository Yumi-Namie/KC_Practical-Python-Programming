

letters = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMÑOPQRSTUVWXYZ " #Incluyo el espacio como letra pos si se admiten frases como pwd
numbers = "0123456789"

pwd = input("pass: ")


def super_debil(pwd):
    res = False
    if len(pwd) < 8:
        res = True
        for i in range(0, len(pwd)):
            res = res and pwd[i] in numbers
    return res

def debil(pwd):
    res = False
    ctde_numbers = 0
    ctde_letras = 0
    if len(pwd) < 8:
        for i in range(0, len(pwd)):
            if pwd[i] in letters:
                ctde_letras +=1
            if pwd[i] in numbers:
                ctde_numbers +=1
        if ctde_numbers >1 and ctde_letras>1:
            res = True
        else:
            False
    return res   

def fuerte(pwd):
    ctde_letras = 0
    ctde_numbers = 0
    res = False
    if len(pwd) >= 8:
        res = True
        for i in range(0, len(pwd)):
            if pwd[i] in letters:
                ctde_letras +=1
            if pwd[i] in numbers:
                ctde_numbers +=1
        if ctde_letras + ctde_numbers == len(pwd):
            res = True
        else:
            res = False
    return res


def super_fuerte(pwd):
    res = False
    ctde_letras = 0
    ctde_numbers = 0
    if len(pwd) >= 8:
        res = True
        for i in range(0, len(pwd)):
            if pwd[i] in letters:
                ctde_letras +=1
            if pwd[i] in numbers:
                ctde_numbers +=1
        if ctde_letras + ctde_numbers != len(pwd):
            res = True
        else:
           res =  False
    return res




def validPwd(pwd):
    if super_debil(pwd):
        print("super debil")
        #return -1 
    if debil(pwd):
        #return 0
        print("debil")
    if fuerte(pwd):
        print("furte")
        #return 1
    if super_fuerte(pwd):
        #return 2
        print("suepr fuerte")



validPwd(pwd)




















   


    

        
    




