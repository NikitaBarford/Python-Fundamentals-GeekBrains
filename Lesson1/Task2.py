""" Task2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк. """

seconds_qty = int(input("Please provide the quantity of seconds: "))
hours = seconds_qty // 3600
minutes = seconds_qty % 3600 // 60
seconds = seconds_qty % 3600 % 60
print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')

