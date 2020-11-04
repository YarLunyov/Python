# Задача №1
# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
# running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
# состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение. Переключение между режимами должно осуществляться только в
# указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
# и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении
# выводить соответствующее сообщение и завершать скрипт.

from time import sleep
from itertools import cycle


class TrafficLight:

    def __init__(self):
        self.__colours = (('красный', 7), ('жёлтый', 2), ('зелёный', 8))

    def running(self):
        for colour, time in cycle(self.__colours):
            print(colour, '(wait {} sec)'.format(time))
            sleep(time)


traffic_light = TrafficLight()
traffic_light.running()


# Задача №2
# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width
# (ширина). Значения данных атрибутов должны передаваться при создании экземпляра
# класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в
# 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        print('Рассчитай массу асфальта')

    def calc(self):
        res = self._length * self._width * 0.025 * 5
        return res


line_segment_1 = Road(20, 5000)
print(line_segment_1.calc())


# Задача №3
# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name ,
# surname , position (должность), income (доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker .
# В классе Position реализовать методы получения полного имени сотрудника ( get_full_name ) и
# дохода с учетом премии ( get_total_income ). Проверить работу примера на реальных данных
# (создать экземпляры класса Position , передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._wage = income['wage']
        self._bonus = income['bonus']


class Position(Worker):
    def get_full_name(self):
        print(self.name + ' ' + self.surname + ', ' + self.position)

    def get_total_income(self):
        print('income ' + str(self._wage + self._bonus))


worker_1 = Position('Пушкин', 'Александр', 'Каменщик', {"wage": 5000, "bonus": 3000})
worker_1.get_full_name()
worker_1.get_total_income()


# Задача №4
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
# color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны
# сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar , SportCar , WorkCar , PoliceCar . Добавьте в базовый класс метод
# show_speed , который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed . При значении скорости свыше 60
# ( TownCar ) и 40 ( WorkCar ) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def going(self):
        print(f'{self.name} let.s go!')

    def stoppy(self):
        print(f'{self.name} let.s stop')

    def turning(self, direction):
        if direction == 'right':
            print(f'{self.name} turning right')
        else:
            print(f'{self.name} turning left')

    def show_speed(self):
        print(f'{self.name} speed = ' + str(self.speed))


class TownCar(Car):
    def show_info(self):
        print(f'it.s {self.color} TownCar')

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Attention! {self.name} speed is higher then MAX!')


class SportCar(Car):
    def show_info(self):
        print(f'it.s {self.color} SportCar')


class WorkCar(Car):
    def show_info(self):
        print(f'it.s {self.color} TownCar')

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Attention! {self.name} speed is higher then MAX!')


class PoliceCar(Car):
    def show_info(self):
        print(f'it.s {self.color} PoliceCar')


sport_car = SportCar(200, 'red', 'SportCar', False)
town_car = TownCar(56, 'green', 'TownCar', False)
work_car = WorkCar(90, 'orange', 'WorkCar', False)
police_car = PoliceCar(210, 'black & white', 'PoliceCar', True)

sport_car.stoppy()
town_car.going()
work_car.show_speed()
police_car.show_info()
sport_car.turning('left')


# Задача №5
# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
# (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
# три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
# реализовать переопределение метода draw. Для каждого из классов метод должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print(f"{self.title} Let's write!")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} Let's draw!")


class Handle(Stationery):
    def draw(self):
        print(f"{self.title} Let's highlight!")


my_pen = Pen('my_pen')
my_pen.draw()

my_pencil = Pencil('my_pencil')
my_pencil.draw()

my_handle = Handle('my_handle')
my_handle.draw()
