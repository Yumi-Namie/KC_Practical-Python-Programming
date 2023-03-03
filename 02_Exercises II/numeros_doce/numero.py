def num_ord(n):
#tuple - secuencia ordendad imutables:
    numeros = ('primero', 'segundo', 'tercero', 'cuarto', 'quinto', 'sexto', 'séptimo', 'octavo', 'noveno', 'décimo', 'undécimo', 'duodécimo')

    if n > 0 and n < 12:
        return numeros[n-1]
    else:
        return ' '



if __name__ == '__main__':

    numeros = ['primero', 'segundo', 'tercero', 'cuarto', 'quinto', 'sexto', 'séptimo', 'octavo', 'noveno', 'décimo', 'undécimo', 'duodécimo']

    for i in range (1,13):
        print("{:2d} -> {}".format(i,numeros[i-1]))


