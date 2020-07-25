"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
 выполнить подсчет количества строк, количества слов в каждой строке."""

f = open("my_file1.txt", "r")
number_of_lines = 0
number_of_words = 0
for line in f:
    line = line.strip("\n")
    words = line.split()
    number_of_lines += 1
    number_of_words += len(words)

f.close()

print("lines:", number_of_lines, "words:", number_of_words)

