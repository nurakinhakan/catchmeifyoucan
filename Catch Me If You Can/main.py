import turtle
import random
import time






normal_tayyip = "normal_tayyip.gif"


#screen setups
wn = turtle.Screen()
wn.setup(700, 700)
wn.title("Agenda in Turkey")
wn.bgcolor("white")
wn.tracer(0)
wn.addshape(normal_tayyip)

text = turtle.Turtle()
text.penup()
text.hideturtle()
text.setposition(-200, 300)
text.write("Please click on the agenda item to remove it", font="Georgia" )



#click turtle
click_turtle = turtle.Turtle()
click_turtle.hideturtle()





sayincumhurbaskanim = turtle.Turtle()
sayincumhurbaskanim.penup()
sayincumhurbaskanim.shape(normal_tayyip)
sayincumhurbaskanim.speed("fastest")
sayincumhurbaskanim.setposition(x=random.randint(-325, 325), y=random.randint(-325, 325))


def random_icon(turtle):
    turtle.goto(x=random.randint(-325, 325), y=random.randint(-325, 325))


def fxn(x, y):
    click_turtle.penup()
    click_turtle.goto(x, y)
    click_turtle.speed("fastest")


def move(turtle1, turtle2):
    if turtle1.distance(turtle2.position()) < 28:
        random_icon(turtle2)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    wn.update()

    wn.onclick(fxn)
    move(click_turtle,sayincumhurbaskanim)


wn.mainloop()