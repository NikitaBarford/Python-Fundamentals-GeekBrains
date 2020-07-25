"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

from random import randint


total = 0
f = open('text5.txt','w')
number = int(input ("How many random numbers do you want to add?: "))
for i in range(number):
    number = randint (1,100)
    number = str(number)+' '
    f.write(number)

f.close()

f1 = open('text5.txt','r')
content = f1.read()
total = 0
for line in content:
    sps = [int(x) for x in content.split()]
    total = sum(sps)


print(f'The sum of numbers equals to: {total}')
f1.close()


