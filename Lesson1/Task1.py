""" Task1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран. """

age_limit = 18
good_drink = "Tea"
bad_drink = "Vodka"
age = int(input("Please inter your age: "))
if age < age_limit:
    print(f"You can only have {good_drink}")
else:
    print(f"You can have {bad_drink} or {good_drink}")
