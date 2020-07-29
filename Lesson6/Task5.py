"""5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпл"""


class Stationery:
    title = 'Super'

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print(f"{self} Pen")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} Pencil")


class Handle(Stationery):
    def draw(self):
        print(f"{self.title} Handle")


s = Stationery()
s.draw()
pn = Pencil()
pn.draw()
h = Handle()
h.draw()
p = Pen()
pn.draw()
