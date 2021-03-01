import turtle
import random
 
wn = turtle.Screen()
tur = turtle.Turtle()
tur.goto(0, 0)
 
def random_walk(kame, n):
    for n in range(n):
        kame.forward(random.randrange(20, 120))
        kame.left(random.randrange(20, 360))
 
random_walk(tur, 30)
     
wn.exitonclick()