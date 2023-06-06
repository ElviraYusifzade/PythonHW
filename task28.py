# Вводится десятичное число. 
# Реализовать алгоритм его перевода в двоичную систему счисления через рекурсию. 
# Нельзя использовать функцию bin()

l = []
def convert(a):
    if (a == 0):
        return l
    dig = a % 2
    l.append(dig)
    convert(a // 2)

n = int(input("Введите число: "))
convert(n)
l.reverse()
print("Двоичная форма числа: ")
for i in l:
    print(i, end = " ")