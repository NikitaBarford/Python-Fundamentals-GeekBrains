"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено."""

from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    print(el)

# ---------------------------------

c = 0
my_list = [2, 5, 4, 55, 5, 34, 35]
for el1 in cycle(my_list):
    if c >= len(my_list):
        break
    c += 1
    print(el1)

