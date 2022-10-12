import turtle

cursor = turtle.Turtle()
cursor.reset()
cursor.up()
cursor.goto(-250, 0)
cursor.down()

cursor.circle(20)
cursor.penup()
cursor.forward(20*2)
cursor.pendown()
cursor.circle(20)

cursor.penup()
cursor.left(90)
cursor.forward(20*2)
cursor.pendown()
cursor.forward(100)
cursor.circle(20, 180)
cursor.forward(100)

turtle.done()