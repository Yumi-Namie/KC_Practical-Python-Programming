import turtle

myTurtleLucy = turtle.Turtle()

sides = input("¿How many sides?")

#No while, ñ podia colocar !=int(sides) xq dava erro de sintaze y no false...
#Tinha que colocar algo que realmente fosse dar false
while sides != "3" or "4":
    try:
        #Tinha que por isso aqui dentro do try y ñ fora
        sides = int(sides)
        
        if sides == 3 or 4:
            for _ in range(0,sides): 
                myTurtleLucy.left(360/sides)
                myTurtleLucy.forward(50)
            break
        
        else:
            print("Sorry. I just know to draw square and triangles")
            break
        
    except ValueError:
        print("The answer should be a number and not a text. Try again")
        sides = input("¿So...How many sides?")



"""
try:
    while sides != int(sides):
        if int(sides) == 3:
            for _ in range(0,sides): 
                myTurtleLucy.left(120)
                myTurtleLucy.forward(50)
            break

        elif int(sides) == 4:
            for _ in range(0,sides):
                myTurtleLucy.forward(50)
                myTurtleLucy.left(90)
            break
        
        else:
            print("Sorry. I just know to draw square and triangles")
    
except ValueError:
    print("The answer should be a number and not a text")
    sides = input("¿How many sides?")
"""

        

    
     
        
       



