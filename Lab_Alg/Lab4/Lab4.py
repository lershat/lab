a = []
k = 0

print("Часть Б. Задание 29. Сортировка фамилий пузырьком")
print("Количество фамилий (целым числом):")
N = int(input())

print("Введите фамилии студентов")
for i in range(N):
    fam = input()
    a.append(fam.capitalize())

for i in range(N - 1):
    for j in range(N - i - 1):
        if a[j] > a[j + 1]:
            #a[j], a[j + 1] = a[j + 1], a[j]
            k = a[j]
            a[j] = a[j + 1]
            a[j + 1] = k

print(a) 