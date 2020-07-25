"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

from googletrans import Translator
t = Translator()


f = open("text_4.txt", "r")
content = f.readlines()
d = {}
for line in content:
    key, value = line.strip().split(" - ")
    d[t.translate(key, dest="ru").text] = value
f.close()


with open("text_4.1.txt", 'w', encoding="utf-8") as f2:
    for key, value in d.items():
        f2.write('%s - %s\n' % (key, value))
f2.close()


