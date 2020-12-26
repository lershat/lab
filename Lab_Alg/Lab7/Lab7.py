# Лабораторная 7

# задача 1
import string, random

def RandSign() :
  mass = []
  a = string.ascii_uppercase + string.ascii_lowercase + string.digits
  for i in range (len (a)) :
    mass.append( a [i] )
  print(random.sample(mass, 10))

RandSign()

#Задача 2
def ren(str):
    return (str[0].split())
 
str = ['For never was a story of more woe than this']
now = ren(str)
spisok = ['u', 'J', 'y', 'W', 'o', 'A', 'm', '2', 'T', 'N']

for i in zip(now, spisok):
   print(i)