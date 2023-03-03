import turtle # T - hay que ser en minuscula

myTurtleLucy = turtle.Turtle()

answerSides = input("How many sides?)")


while True: 
    try:
        sides= int(answerSides)
        answerSize = input("Which size? S(small) / M(mediun) / B(big))")
        break
    except ValueError:
        print("oops! You cannot write a text, just numbers. Try again")
        answerSides = input("So...How many sides?)")    
    
    

while True:
    letSize = answerSize.upper()
    numSize = 0

    if letSize != 'S' and letSize !='M' and letSize !='B':
            print("Ops! You cannot add another size. Try again")
            answerSize = input("So...Which size? S(small) / M(mediun) / B(big))")

    else:

        if letSize == 'S':
            numSize = 30
        elif letSize == 'M':
            numSize = 50
        elif letSize == 'B':
            numSize = 80
        break

for _ in range(0,sides):
        myTurtleLucy.forward(numSize)
        myTurtleLucy.left(360/sides)


turtle.done()
