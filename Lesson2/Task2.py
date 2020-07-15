my_list = list(input("Input your numbers: "))

for i in range(0, len(my_list), 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)

"""Простите пожалуйста, решение стырил и не успел до ума довести работу с нечётным кол-вом мемберов :("""
