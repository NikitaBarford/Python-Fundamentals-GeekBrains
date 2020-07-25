"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

f = open("text_3.txt", "r")
content = f.readlines()
d = {}
for line in content:
    key, value = line.strip().split(" ")
    d[key] = float(value)
    if float(value) < 20000:
        d[key] = float(value)
        print(f'{key}:' + "${:.2f}".format(float(value)))

mean = sum(d.values()) / len(d)

print(f'Средняя зарплата всех сотрудников: ${mean}')


f.close()



