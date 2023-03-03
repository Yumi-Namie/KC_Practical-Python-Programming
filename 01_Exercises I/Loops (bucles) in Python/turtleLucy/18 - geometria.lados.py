import turtle

myTurtleLucy = turtle.Turtle()


sides = input("¿Cuantos lados quieres?")

if sides == '3':
    for _ in range(0,3): 
        myTurtleLucy.left(120)
        myTurtleLucy.forward(50)
        
    
elif sides == '4':
    for _ in range(0,4):
        myTurtleLucy.forward(50)
        myTurtleLucy.left(90)
        
