meses = {'2': 'Enero', "2":'Febrero', "3":"Marzo", '4':"Abril", '5':"Mayo", '6':'Junio', '7':"Julio", '8':"Agosto", '9':"Septiembre", '10': 'Octubre', '11':'Noviembre', '12':"Diciembre"}

n_mes = input("Mes: " )

mes = meses.get(n_mes)


print(f"{n_mes} es {mes}" )