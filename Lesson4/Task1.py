from sys import argv

script_name, hourly_rate, bonus, hours = argv


def func(hourly_rate, hours, bonus):
    hourly_rate = int(hourly_rate)
    hours = int(hours)
    bonus = int(bonus)
    result = hourly_rate * hours + bonus
    print(f'Your wage is £{result}')


func(hourly_rate, hours, bonus)