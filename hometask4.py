# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов. Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
k = int(input('type k: '))
f0, f1  = 0, 1
fib_list = [f0, f1]
for i in range(k - 1):
    f2 = f0 + f1
    fib_list.append(f2)
    f0, f1 = f1, f2
fib_negativ = fib_list[1:]
fib_negativ.reverse()
for i in range(len(fib_negativ)):
    fib_negativ[i] *= -1
new_fib = fib_negativ + fib_list
print(*new_fib)

