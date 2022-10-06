# Задача №4.
# Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен
# степени k. *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from calendar import c
import os
os.system("cls")
from random import randint
import itertools

k = int(input('Задайте натуральную степень k: '))

ratio_list = list([randint(0, 101) for i in range(k+1)]) # задаем случайный список
if ratio_list[0] == 0: # если будет равен 0, томногочлен может быть неверным
    ratio_list[0] = randint(1, 101)
print(ratio_list)

def get_polynomial(k, ratio_list): # далее идет загугливание информации
    str1 = ['*x**']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratio_list, str1, range(k, 1, -1), fillvalue = '') if a !=0]
    # с помощью этого метода мы объединяем несколько списков в список кортежей с самой длинной итерацией
    # пустые кортежи заполняем пустотой ('')
    print(polynomial)
    for x in polynomial:
        x.append(' + ') # проставляем + между кортежами
    polynomial = list(itertools.chain(*polynomial)) # объединяем в один список
    print(polynomial)
    polynomial[-1] = ' = 0' # добавляем концовочку (меняем последний '+' на '= 0')
    return "".join(map(str, polynomial)).replace(' 1*x',' x') # возвращаем строку

list = get_polynomial(k, ratio_list)
print(list)

with open('file.txt', 'w') as data:
    data.write(list)
with open('file.txt', 'w') as data:
    data.write(list)
