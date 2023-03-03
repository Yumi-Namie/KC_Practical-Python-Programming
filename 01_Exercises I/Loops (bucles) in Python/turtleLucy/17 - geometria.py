import turtle

myTurtleLucy = turtle.Turtle()


answer = input("¿Quieres un triángulo? (S / N)")
answer = answer.upper()


if answer == "S":
    for _ in range(0,3): 
        myTurtleLucy.left(120)
        myTurtleLucy.forward(50)
    
else:
    for _ in range(0,4):
        myTurtleLucy.forward(50)
        myTurtleLucy.left(90)