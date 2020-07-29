"""4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат."""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Current speed is {self.speed} miles per hour')

    def go(self):
        print(f'The car is moving now')

    def stop(self):
        print(f'The car is stopped')

    def direction(self, direction):
        print(f'The car is moving to the {direction}')


class TowCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Current speed is too high!!')
        else:
            print(f'Current speed is {self.speed} miles per hour')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Current speed is too high!!')
        else:
            print(f'Current speed is {self.speed} miles per hour')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


c = Car(30, "White", "Audi", False)
print(f'Your {c.color} {c.name} is moving at {c.speed} miles per hour')
tc = TowCar(61, "White", "Audi", False)
tc.show_speed()
c.stop()
c.direction("left")


