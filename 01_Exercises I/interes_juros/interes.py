
def calc_interes():
    tax = float(interes)/100
    invest = round(float(inv),2)
    years = float(anos)
    return invest* (1.0 +tax*years)


if __name__ == '__main__':
    inv = input("Valor invertido: ")
    anos = input("Años transcorridos: ")
    interes = input("Interés anual: ")

    print(f"Tras {anos} años de inersión al {interes} %, su cantidad debe ser {calc_interes():.2f}€")