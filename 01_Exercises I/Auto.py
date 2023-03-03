class Rectangulo():
    """
    Escrita orientativo llamado de docstring, podendo ser evocado con print(Auto.__doc__)
    """
    def __init__(self, base=1, altura=1, color= "rojo"):
        self.base= base
        self.altura = altura
        self.color = color
    
    #instancias
    def perimetro(self):
        return 2*self.base + 2*self.altura
    
    def area(self):
        return self.base*self.altrua

"""
practica
"""

forma1= Rectangulo(5,2,"azul")
print("El perimetro es {}".format(forma1.perimetro()))

