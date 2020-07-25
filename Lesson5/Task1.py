"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных свидетельствует пустая строка."""

f = open("my_file.txt", 'w+')
while True:
    inp = input("Inter some text:\n")
    f.write(f'{inp} \n')
    if inp == " ":
        break
    else:
        continue
f.close()
print("Ввод завершён")
