
n1 = input ("Dime un primer número ")
n2 = input ("Ahora dime un otro número ")


while True:
    try:
        n2 = float(n2)
        n1 = float(n1)
        if n1<=0 or n2 <=0:
            print("Oop!Por favor solo nº POSITIVOS")
            n1 = input ("Dime un primer número ")
            n2 = input ("Ahora dime un otro número ")    
        else:
            break

    except ValueError:
        print("Error:\nDebe ingresar NÚMEROS")
        n1 = input ("Dime un primer número ")
        n2 = input ("Ahora dime un otro número ")


print("\n {} + {} = {}\n {} - {} = {}\n {} x {} = {}\n {} % {} = {}".format(n1, n2, n1+n2, n1, n2, n1-n2, n1, n2, n1*n2, n1, n2, n1/n2))
