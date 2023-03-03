#Crear un prog que devuleva los codigos ASCII de los caracteres desde el 32 al 127.
def caracteres():
    for i in range(32, 128):
        print("'{}' : {:3d}".format(chr(i),i), end="\t") 
        if i % 4 == 3:
            print("")

#Por default los print tienen dentro de su funcion un \n, o sea, un saltador de linea.
#Dibujando las columnas, sabemos que los 4 numeros serian 32, 33,34 y 35. Luego tendria que saltar la linea.
#Para este ejercicio, solo cuando llegase en nº "35": saltaria la linea y asi por delante
# Para llegar a eso, solo era dividir el numero 35 (que estaria en la cuarta columna) y sabreria el resultado. 35 %4 == 3 (resta 3)
#Cuando colomos el end en en final, sustituyimos el saltador \n (default) por tab (un espazador), de esta manera..seguimos en la misma linea...
#Es posible perceber que el espacio entre columnas no controlamos la distancia, xq es el tab (espacio que por default son 4 casillas)
#Luego, colocamos un print de un texto vacío " " y que automaticamente, salta la linea
#el format :3d significa alinhar d (nº entero) 3 casillas. 



if __name__ == '__main__':
    caracteres()