import turtle as t
tsize = 40

clist = ['violet','indigo','blue','green','yellow','orange','red']
length = 40
x=0


for color in clist:
    t.pensize(tsize)
    t.up()
    t.goto(x+length,0)
    t.down()
    t.seth(90)
    t.color(color)
    t.circle(length,180)
    length += 40
    tsize +=1


t.done()