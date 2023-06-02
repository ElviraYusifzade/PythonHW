# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

import random
n = int(input("Введите размер массива: "))
x = int(input("Введите искомое число x: "))
arr = []
for i in range(n):
    arr.append(random.randrange(n))
print(arr)
def nearval(arr, number):
    return min(arr, key=lambda x: abs(number - abs(x))) 
print(f'Ближайшее к {x} число в массиве: {nearval(arr, x)}')
