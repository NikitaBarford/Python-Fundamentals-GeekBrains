"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""


def pers(name, surn, year, town, mail, tel):
    z = (f"Dear {surn} {name},you were born in {year}, in a beatiful city of {town}, here is your email:{mail} and your telephone number {tel}")
    print(z)

pers(name = input("Please provide you name: "),surn = input("Please provide you surname: "), mail = input("Please provide you email: "),
     year = input("Please provide date of birth: "),tel = input("Please provide you phone number: "),town = input("Please provide you City: "))
