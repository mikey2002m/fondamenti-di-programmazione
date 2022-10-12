# ALBERO BINARIO
import turtle


def tree(cur: turtle.Turtle, leng, level):
    if level == 0:
        cur.color('yellow')
        cur.dot(5)
        cur.color('black')
        return
    cur.fd(leng)
    cur.left(30)
    tree(cur, leng*0.8, level-1)

    cur.right(30+30)
    tree(cur, leng*0.8, level-1)
    cur.left(30)
    cur.backward(leng)


cursor = turtle.Turtle()
cursor.reset()
cursor.up()
cursor.goto(-250, 0)
cursor.down()
cursor.speed(10)
tree(cursor, 100, 8)

turtle.done()

