
def conversor(tipo, temp):
    
        if tipo == "F":
            entrada = 'Celsius'
            salida = 'Fahrenheit'
            result = (temp - 32)*5/9
            
        elif tipo == "C":
            entrada = 'Fahrenheit'
            salida = 'Celsius'
            result = (temp*9/5) + 32

        else:
            print("Error")                

        return entrada, result, salida


def str_upper (texto):
    return input(texto).upper()

def str_number (texto):
    while True:
        try:
            return float(input(texto))
        except ValueError:
            print("Digitar solamente números")

if __name__ =='__main__':
    inputTipo = str_upper("Quieres converter a Fahrenheit o Celsius? (F/C) ")
    inputTemp = str_number("Valor de la temperatura: ")

    entrada, result, salida = conversor(inputTipo,inputTemp)

    print(f"{inputTemp}º {entrada} son {result:.2f} {salida}")