from academia import Alumno, Asigntaura, Profesor

roberto = Alumno ('Roberto', 'Rodríguez')
susana = Alumno ('Susana', 'Martín')

print(roberto.nombre, roberto.apellidos, roberto) # Roberto Rodriguez
print(susana.nombre, susana.apellidos, susana) # Susana Martín

print(roberto.correo_e, roberto.movil) 

#Asignturas y valores#
ingles = Asigntaura('Inglés', 'A2')
ingles.precio_h = 7.5

aleman = Asigntaura('Alemán', 'A2')
aleman.precio_h = 8

chino = Asigntaura('Chino Cantonés', 'A1')
chino.precio_h = 10


print(ingles) #asignatura: Inglés - A2 - (30 €/mes)

roberto.alta_asignatura(ingles)
roberto.alta_asignatura(chino)


print(roberto.asignaturas)
print(susana.asignaturas)

donJose = Profesor("José", "Martín Fusta", "0W", "jf@gmail.com")
print(donJose) #Profesor: 0W - José Martín fusta - jf@gmail.com

print(donJose.sueldo()) #200

donJose.alta_asignatura(ingles)

print(donJose.asignaturas) # asignatura: Inglés - A2 - (30 €/mes)
print(donJose.sueldo()) #500