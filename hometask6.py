# Реализуйте алгоритм перемешивания списка.
import random
from random import randrange #можно рандомно задавать
orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]# [randrange(1, 10) for i in range(10)]
print('Original list is: ' + str(orig_list))
for i in range(len(orig_list)):
    j = random.randint(0, i + 1)
    orig_list[i],orig_list[j] = orig_list[j], orig_list[i]
print('The shufled list is: '+ str(orig_list))