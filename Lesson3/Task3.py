"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов."""


def my_func(var_1, var_2, var_3):
    var_4 = [var_1, var_2, var_3]
    var_4.sort()
    result = sum(var_4[1:])
    return result


print(my_func(40, 20, 80))
