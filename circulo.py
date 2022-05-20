from turtle import *
color = ['orange','red','pink','yellow','blue','green'] 
for x in range(360):
    pencolor(color[x % 6])
    width(x / 5 +1)
    forward(x)
    left(35)
