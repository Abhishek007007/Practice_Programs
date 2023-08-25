import turtle

t = turtle.Turtle()
lenghth = 50
for i in range(20):
    t.forward(lenghth)
    t.right(90)
    if((i+1)%2 == 0):
        lenghth += 25


turtle.done()

