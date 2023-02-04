# Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N. Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
n = int(input('type N: '))
count = 1
result = 1
multi_list = []
while count <= n:
    result *= count
    multi_list.append(result)
    count += 1
print(*multi_list)
