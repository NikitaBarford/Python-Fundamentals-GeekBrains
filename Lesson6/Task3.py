"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров)."""


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {}


class Position(Worker):
    def get_full_name(self, name, surname):
        print(f'{name} {surname}')

    def get_total_income(self):
        self._income = {"Wage": 100, "Bonus": 20}
        print(f'Your income = {sum(self._income.values())}')


p = Position()
p.get_full_name('Ivan', "Petrov")
p.get_total_income()