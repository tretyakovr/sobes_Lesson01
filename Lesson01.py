# Третьяков Роман Викторович
# Факультет Geek University Python-разработки
# Урок 1. Задание 1:
#  Написать функцию (несколько функций), реализующую вывод таблицы умножения размерностью AｘB.
#  Первый и второй множитель должны задаваться в виде аргументов функции.

import sys

def checkParam(param):

    try:
        retval = int(param)
    except:
        print(f'Ошибка преобразования параметра {param} к целочисленному положительному ненулевому значению!')
        retval = 0
    else:
        if retval != param:
            print(f'Предупреждение: параметр {param} преобразован к целочисленному значению {retval}!')

        if retval <= 0:
            print('Ошибка: параметром передано не целое положительное число!')
            retval = 0

    return retval

def multiplication_table(a, b):

    a = checkParam(a)
    b = checkParam(b)

    if a and b:
        for i in range(1, a+1):
            for j in range(1, b+1):
                print(f'{i : 3} \t x \t {j : 3} \t = \t {i * j : 3}')

multiplication_table('sdcsd', -1);