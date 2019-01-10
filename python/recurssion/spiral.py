import turtle

myTurtle = turtle.Turtle()
myScreen = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(-45)
        drawSpiral(myTurtle, lineLen - 1)


drawSpiral(myTurtle, 100)



