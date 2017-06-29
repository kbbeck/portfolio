from turtle import *

sides = int(input("Enter number of sides:"))
sizes= input("Enter pen size:")
colors = input("Enter color:")
pensize(sizes)
pencolor (colors)
fillcolor (colors)
angle= 360/sides
print("sides:", sides, "angle:", angle)
begin_fill()
for side in range(sides):
    forward(100)
    right(angle)
end_fill()
exitonclick()
