import turtle

turtle.shape('turtle')

st1 = 0
st2 = 0
k = 0
m = 0

def pr(st1, st2):
  turtle.pendown()
  i = 0
  if st2 == 0:
    while i < 4:
      turtle.forward(st1)
      turtle.left(90)
      i += 1
    i = 0
  else:
    while i < 2:
      turtle.forward(st1)
      turtle.left(90)
      turtle.forward(st2)
      turtle.left(90)
      i += 1
    i = 0
  turtle.penup()

def sdvig(s1,s2):
  turtle.forward(s1)
  turtle.right(90)
  turtle.forward(s2)
  turtle.left(90)

# Чашка
turtle.goto(-100,0)
while k < 5:
  pr(100-m,20)
  sdvig(10,20)
  m += 20
  k += 1

# Блюдце
turtle.goto(-110,-90)
pr(120,10)

# Ручка
turtle.goto(-10,-50)
pr(50,0)
sdvig(10,-10)
pr(30,0)