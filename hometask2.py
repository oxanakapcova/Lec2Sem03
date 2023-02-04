# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний
# элемент, второй и предпоследний и т.д. Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randrange
n = int(input('type amount: '))
my_list = [randrange(1, 10) for i in  range(n)]
print(my_list)
new_list = []
if len(my_list)%2 == 0:
    for i in range(len(my_list)//2):
        new_list.append(my_list[0] * my_list[-1])
        del my_list[0]
        if len(my_list) > 0:
            del my_list[-1]
else:
    for i in range(len(my_list)//2 + 1):
        new_list.append(my_list[0] * my_list[-1])
        del my_list[0]
        if len(my_list) > 0:
            del my_list[-1]

print(new_list)

