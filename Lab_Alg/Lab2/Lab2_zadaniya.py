#1
bots = 1000
DelInDay = 2
AddDay = 3
NDay = 30

print("Задание 1")
print("Если будет добавлять, ботов будет ", bots - DelInDay*NDay + AddDay*NDay, ", иначе - ", bots - DelInDay*NDay)


#2
HeightHome = 3
WidthStake = 4
Add = 1.5
Ends = 2
Rope = 0

print("Задание 2")
Rope = (HeightHome**2 + WidthStake**2)**0.5 + Add*Ends
print("Необходимая длина веревки: ", Rope, "метров")


#3
SHomeYuri = 7*9 - 3*2
SHomeVlad = (9/2)*2*3.14

print("Задание 3")
print("Площадь дома больше у Юрия, чем у Владимира это Истина (",SHomeYuri>SHomeVlad, ")")


#4
VAuto = 30*3.6
VPesh = 4
TAuto = 1/6
AB = VAuto*TAuto
TPesh=AB/VPesh

print ("Задание 4")
print("Расстояние от А до В - ", AB, ". Полное время, которое потребуется пешеходу - ", TPesh, "часа, а если он уже прошел 2 часа, то ему осталось - ", TPesh-2, "часа.")


#5
StAuto = 11000
All = StAuto*4
Bank = All/4
Trat = All*0.15
Ost = All - StAuto - Bank - Trat

print("Задание 5")
print("Осталось: ", Ost)


#6
Otvet = (((60-(14+16))/5)**(22-19))
print("Задание 6")
print("Ответ: (((60-(14+16))/5)**(22-19)) = ", Otvet)

#7
print("Задание 7")
print("fanat" > "apple", "fanat" > "abracadabra", "fanat" > "Tarantino", "fanat" > "yahoo", "yahoo" > "yandex", "yandex" > "gool", "yandex" > "logo", "yandex" > "fanat")
print("Самое большое - yandex")