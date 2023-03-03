sueldos = (12450, 20200, 35200, 60000, 70000, 100000,10000000)
retenciones = (1.55, 13.32, 20.08, 26.84, 29.91, 33.94, 44.88)

def buscaRetencion(s):
    puntero = 0

    while puntero <7 and s >= sueldos[puntero]:
        puntero = puntero + 1

    if puntero == 0:
        irpf = 0
    elif puntero ==7:
        irpf = 45
    else:
        irpf = retenciones[puntero-1] + ((s - sueldos[puntero-1])*(retenciones[puntero]-retenciones[puntero-1])/ (sueldos[puntero]-sueldos[puntero-1]))

    return irpf

def netoAnual(s, r):
    irpfTotal = r + 6.35
    miSueldoNeto = s * (100-irpfTotal)/100
    return miSueldoNeto