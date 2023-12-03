import turtle

# Set the turtle's speed to the maximum
turtle.speed(0)

# Set the background color
turtle.bgcolor("black")

# Set the starting position of the turtle
turtle.penup()
turtle.setpos(-200, 0)
turtle.pendown()

# Set the turtle's color
turtle.color("red")

# Draw the rose
for i in range(200):
    turtle.forward(200)
    turtle.left(170)

# Hide the turtle
turtle.hideturtle()

# Keep the window open until the user clicks
turtle.exitonclick()
