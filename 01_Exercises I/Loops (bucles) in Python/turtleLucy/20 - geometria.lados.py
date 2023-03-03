import turtle

myTurtleLucy = turtle.Turtle()

class ThirteenSidesInvalid(Exception):
    pass

sides = input("¿How many sides?")

if sides == "13":
    raise ThirteenSidesInvalid("You cannot add 13 sides!")

while True:
    try:
        sides = int(sides)
        break
    except ValueError:
        print("aviso")
        sides = input("¿So...How many sides?") 

for _ in range(0, sides):
    myTurtleLucy.forward(50)
    myTurtleLucy.left(360/sides)

