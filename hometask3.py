# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
number = int(input('type number: '))
count = 0
# el = 0
binary_list = []
while number > 0:
    el = number % 2
    binary_list.append(el)
    number //= 2
binary_list.reverse()
print(*binary_list) #print(reversed(binary_list))


