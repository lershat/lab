import turtle
 
def sur_draw(size, n):
    if n == 0:
        turtle.forward(size)
    else:
        sur_draw(size / 3, n - 1)
        turtle.right(75)
        sur_draw(size / 3, n - 1)
        turtle.left(120)
        sur_draw(size / 3, n - 1)
        turtle.right(75)
        sur_draw(size / 3, n - 1)
 
 
def sureken(size, n):
    for i in range(4):
        sur_draw(size, n)
        turtle.right(120)
 
turtle.left(180) 
sureken(100, 2)
