#Crear class para nodo que tiene un valor (la pregunta) con dos salidas de respuestas

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.leftChild = None
        self.rightChild = None
    #Convertir en valor y no un espacio de la memoria
    def __repr__(self):
        return self.valor

def datos_arbol ():
    #Colocando valores en los nodos  -> self.valor = valor      
    n1 = Node(("Arranca? "))
    n2 = Node(("Suena un clic-clic? "))
    n3 = Node(("Están los bornes de ka batería corroídos? "))
    n4 = Node(("Reemplaza la bateria. "))
    n5 = Node(("Se enciende el coche pero no arranca? "))
    n6 = Node(("Limpia los bornes y arranca de nuevo "))
    n7 = Node(("Reemplaza los cables y arranca de nuevo "))
    n8 = Node(("Revisa las bujías "))
    n9 = Node(("¿Arranca el coche y luego se cala? "))
    n10 = Node(("¿Es un coche de inyección "))
    n11 = Node(("Lleve el coche al taller"))
    n12 = Node(("Abra y cierre el starter"))

    #Añadindo los internals nodes (child nodes/leaf nodes) -> colocando valores en sel.leftChild & self.rightChild
    n1.leftChild = n2
    n1.rightChild = n3
    n2.leftChild = n4
    n2.rightChild = n5
    n3.leftChild = n6
    n3.rightChild = n7
    n5.leftChild = n8
    n5.rightChild = n9
    n9.leftChild = n10
    n10.leftChild = n11
    n10.rightChild = n12

    return n1


#Colocando para funcionar
def binaryTree(root_node: Node) -> Node:
    pregunta: Node = root_node
    
    while pregunta.leftChild != None or pregunta.rightChild != None:
        respuesta: str = input(pregunta.valor).upper()

        if respuesta == 'S':
            pregunta = pregunta.leftChild
        elif respuesta == 'N':
            pregunta = pregunta.rightChild

    return pregunta



if __name__ == '__main__':
    root_node = datos_arbol()
    solucion: Node = binaryTree(root_node)
    print("Entonces... {}".format(solucion))





