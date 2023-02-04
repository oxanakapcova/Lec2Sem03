# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1, 2, 3, 4, 5
# 3
# -> 1

my_list = [int(input('type number: ')) for i in range(int(input('type amount: ')))]
print(my_list)
x = int(input('type X: '))
# solution 1:
if x in my_list:
    print(my_list.count(x))
else:
    print(f'There is no any {x}')
# solution 2:
exit() # для компилятора
count = 0
for number in my_list:
    if x == number:
        count += 1
print(count)

