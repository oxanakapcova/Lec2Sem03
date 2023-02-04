# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции. Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
my_list = [int(input('type element: ')) for i in range(int(input('type amount: ')))]
print(my_list)
new_list = my_list[1::2]
print('На нечетных позициях стоят элементы: ')
print(*new_list)
sum = 0
for i in new_list:
    sum +=i
print(f'Сумма элементов равна {sum}')
