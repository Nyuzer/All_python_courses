# OOP
# example
"""class Car:
    model = 'BMW'
    engine = 1.6"""

# Атрибуты
"""class Person:
    name = "Ivan"
    age = 30
print(Person.__dict__)"""

# getattr
"""class Person:
    name = 'Ivan'
print(getattr(Person, 'name'))"""
# getaatr(Person, 'age', 100)   -   3 колонка значит что будет выведено, если нет какого-то атрибута.

# Динамическое создание атрибутов класса.
"""class Person:
    pass
Person.x = 100
print(Person.x)"""

# setattr
"""class Person:
    pass
setattr(Person,'z', 5000)
print(Person.z)"""

# 1 Удаление атрибута в классе
"""class Person:
    pass
setattr(Person,'z', 5000)
del Person.z
print(Person.__dict__)"""
# 2
"""class Person:
    name = 'Ivan'
delattr(Person, 'name')"""

"""class Car:
    model = 'BMW'
    engine = 1.6

a1 = Car()
a1.seat = 4"""

# вызов функции внутри класса getattr()
"""class Car:
    model = 'BMW'
    engine = 1.6

    def drive():
        return "Let's GO!"

print(getattr(Car,'drive')())"""

# Конструкторы
"""class Point():
    def __init__(self, x = 0, y = 0):
        print('создание экземпляра класса Point')
        self.x = x
        self.y = y

    def setCoords(self,x,y):
        print(self.__dict__)
        self.x = x
        self.y = y

pt = Point()
pt2 = Point(6)
pt3 = Point(5, 10)
print(pt.__dict__, pt2.__dict__, pt3.__dict__, sep = '\n')
"""
# pt.setCoords(5,10) == Point.setCoords(pt,5,10)

# Деструкторы
"""class Point():
    def __init__(self, x = 0, y = 0):
        print('создание экземпляра класса Point')
        self.x = x
        self.y = y

    def __del__(self):
        print('удаление экземпляра' + self.__str__())

    def setCoords(self,x,y):
        print(self.__dict__)
        self.x = x
        self.y = y

pt = Point()
pt2 = Point(6)
pt3 = Point(5, 10)
print(pt.__dict__, pt2.__dict__, pt3.__dict__, sep = '\n')"""

"""class Lion():
    def __init__(self):
        pass

    def roar(self):
        print("Rrrrrrr!!!")

simba = Lion()
simba.roar() """

# 1
"""class Counter():
    def start_from(self, x = 0):
        self.x = x

    def display(self):
        print(f"Текущее значение счетчика = {self.x}")

    def increment(self):
        self.x += 1

    def reset(self):
        self.x = 0"""

# s = ((x2-x1)**2+(y2-y1)**2)**0.5

"""class Point():
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, another):
        if isinstance(another, Point):
            print(((another.x - self.x) ** 2 + (another.y - self.y) ** 2)**0.5)
        else:
            print('Передана не точка')"""

# Magick methods
"""class Cat():
    def __init__(self, name, breed = 'siam', age = 1, color = 'white'):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
tom = Cat('Tom', age = 10)
print(tom.__dict__)"""

"""class Laptop():
    def __init__(self,brand = '',model = '',price = 0):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = brand + ' ' +  model"""

"""class SoccerPlayer():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, goals=1):
        self.goals += goals

    def make_assist(self, assists=1):
        self.assists += assists

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')
s = SoccerPlayer('n','s')"""

# 1
"""class Zebra():
    x = 0
    def which_stripe(self):
        l = ["Полоска белая" , "Полоска черная"]
        if self.x == 0:
            print(l[self.x])
            self.x = 1
        else:
            print(l[self.x])
            self.x = 0
"""

# 2
"""class Zebra:
    flag = True
    def which_stripe(self):
        print('Полоска белая' if self.flag else 'Полоска черная')
        self.flag = not self.flag"""

"""class Person():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def is_adult(self):
        return self.age >= 18"""

# Cтатические свойства и методы классов, декоратор, Приват
"""class Point():
    __count = 0
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super(Point, cls).__new__(cls)
            print(1)
        else:
            print('Экземпляр класса Point уже создан!')

    def __init__(self, x=0, y=0):
        Point.__count += 1
        self.coorx = x
        self.coory = y"""

"""class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, say):
        return f'{self.name} says {say}'

"""

"""class Stack():
    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)

    def pop(self):
        if len(self.values) >= 1:
            return self.values.pop()
        elif len(self.values) == 0:
            print('Empty Stack')

    def peek(self):
        if len(self.values) >= 1:
            return self.values[-1]
        else:
            print('Empty Stack')
            return

    def is_empty(self):
        return len(self.values) == 0


    def size(self):
        return len(self.values)
"""

"""class Cat:
    __share_attr = {
        'breed' : 'pers',
        'color' : 'black'
    }
# с помощью атрибута share_attr значения экземпляров меняются у всех остальных экземплярах
    def __init__(self):
        self.__dict__ = Cat.__share_attr

d = Cat()
g = Cat()

d.breed = 'siam'
d.name = 'Bob'
h = Cat()
print(h.__dict__)"""

# Инкапсуляция - механизм языка, позволяющий объединить данные и методы, работающие с этими данными,
# в единый объект и скрыть детали реализации от пользователя.
# Публичный, приватный, защищенные атрибуты

"""class BankAccount:
    def __init__(self, name, balance, passport):
        self.__name = name   # c _ это защищенные атрибутты
        self.__balance = balance    # c __ это приватные атрибуты
        self.__passport = passport

    def print_public_data(self):
        self.__print_private_data()

    def print_protected_data(self):
        print(self._name, self._balance, self._passport)

    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)

account1 = BankAccount('Nikita', 10000, 4542423)
account1._BankAccount__print_private_data()
print(account1._BankAccount__balance)"""

# геттеры и сеттеры
"""class Point:
    WIDTH = 5
    __slots__ = ['__x', '__y']  # указываем любые локальные свойства наших экземпляров класса
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __checkValue(a):
        if isinstance(a, int) or isinstance(a, float):
            return True
        return False

    def setCoords(self, x , y):
        if Point.__checkValue(x) and Point.__checkValue(y):
            self.__x = x
            self.__y = y
        else:
            print('Координаты должны быть числами!')

    def getCoords(self):
        return self.__x,self.__y
"""
"""    def __getattribute__(self, item):
        if item == '_Point__x':
            return 'Частная переменная'
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'WIDTH':
            raise AttributeError
        else:
            self.__dict__[key] = value  # так нужно менять данные в переменных

    def __getattr__(self, item):
        print('__getattr__ ' + item)

    def __delattr__(self, item):
        print('__delattr__ ' + item)"""
"""
p = Point(1, 2)
print(p.getCoords())
p.setCoords(10, 20)
print(p._Point__x)
# p.setCoords('10', 20)
#p.WIDTH = 10
# _<имя класса>__<имя метода или переменной>"""

# Property
"""class CoordValue:
    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        self.__value = value

    def __delete__(self, instance):
        del self.__value



class Point:
    coordX = CoordValue()
    coordY = CoordValue()

    def __init__(self, x=0, y=0):
        self.coordX = x
        self.coordY = y

    def __checkValue(x):
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    @property
    def coordX(self):
        return self.__x

    @coordX.setter
    def coordX(self, x):
        if Point.__checkValue(x):
            self.__x = x
        else:
            raise ValueError('Неверный формат данных')

    @coordX.deleter
    def coordX(self):
        print('Удаление свойства')
        del self.__x

    #coordX = property(__getCoordX, __setCoordX, __delCoordX)

p = Point(1,2)"""


"""class CoordValue:
    def __set_name__(self, owner, name):
        print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value

class Point:
    coordX = CoordValue()
    coordY = CoordValue()

    def __init__(self, x=0, y=0):
        self.coordX = x
        self.coordY = y

p = Point(1, 2)
p2 = Point(5, 10)
print(p.coordX, p.coordY)
print(p2.coordX, p2.coordY)"""

"""class UserMail():
    def __init__(self, login, mail):
        self.login = login
        self.__email = mail

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, mail):
        if isinstance(mail, str) and mail.count('@') == 1 and \
        mail.count('.') == 1 and (mail.find('@') < mail.find('.')):
            self.__email = mail
        else:
            print('Ошибочная почта')"""

"""class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    
    @property
    def my_balance(self):
        print('get balance')
        return self.__balance
    
    @my_balance.setter
    def my_balance(self, x):
        print('Set balance')
        if not isinstance(x, (int,float)):
            raise ValueError('Баланс должен быть числом!')
        else:
            self.__balance = x
    
    @my_balance.deleter
    def my_balance(self):
        print('delete balance')
        del self.__balance"""

"""class Money():
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) and value >= 0:
            self.total_cents = value * 100 + (self.total_cents % 100)
        else:
            print('Error dollars')

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and 100 > value >= 0:
            self.total_cents = (self.total_cents // 100) * 100 + value
        else:
            print('Error cents')

    def __str__(self):
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'"""

"""class Square():
    def __init__(self, x):
        self.__side = x
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.__side ** 2
        return self.__area"""

# @classmethod  @staticmethod

"""class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    def setCoords(self, x, y):
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y

    @classmethod
    def validate(cls, arg):
        if arg >= cls.MIN_COORD and arg <= cls.MAX_COORD:
            return True
        return False

    @staticmethod
    def norm2(x, y):
        return x*x + y*y"""


"""class Robot:
    population = 0

    def __init__(self, name):
        self.__name = name
        Robot.population += 1
        print(f'Робот {self.__name} был создан')

    def destroy(self):
        print(f'Робот {self.__name} был уничтожен')
        Robot.population -= 1
        del self.__name

    def say_hello(self):
        print(f'Робот {self.__name} приветствует тебя, особь человеческого рода')

    @staticmethod
    def how_many():
        print(f'{Robot.population}, вот сколько нас еще осталось')"""

# можно еще через класс метод

"""    @classmethod
    def how_many(cls):
        print(f'{cls.population}, вот сколько нас еще осталось')"""

"""class User:
    password_path = 'password.txt'

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if self.is_secure_password(value):
            self.__password = value
        else:
            raise ValueError('Небезопасный пароль')

    @staticmethod
    def is_secure_password(value):
        file =  open('password.txt', 'r', encoding='utf-8')
        password_dict = map(str.strip, file.readlines())
        if value in password_dict:
            return False
        else:
            return True"""

# Маг. методы __str__   __repr__

"""class Lion:
    def __init__(self, name):
        print('hello')
        self.name = name

    def __repr__(self):
        return f'The object Lion - {self.name}'

    def __str__(self):
        return f'Lion - {self.name}'

q = Lion('Bob')"""

"""class Person:
    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        if gender in ['male','female']:
            self.gender = gender
        else:
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
            self.gender = 'male'

    def __str__(self):
        if self.gender == 'male':
            return f'Гражданин {self.surname} {self.name}'
        else:
            return f'Гражданка {self.surname} {self.name}'"""

"""class Vector:
    def __init__(self, *args):
        self.values = []
        for i in args:
            if isinstance(i, int):
                self.values.append(i)

    def __str__(self):
        if len(self.values) != 0:
            return f'Вектор{tuple(sorted(self.values))}'
        return 'Пустой вектор'"""

# __abs__   __len__

"""class Vector:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))"""

#  __add__  __mul__     __sub__    __truediv__

"""class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__ call')
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return BankAccount(self.name, self.balance + other)
        raise NotImplemented

    def __repr__(self):
        return f'{self.name} - {self.balance}'

b = BankAccount('Sanya', 12000)
s = BankAccount('Sisa', 12500)
print(s + 121)
print(b + s)"""

"""
class Vector:
    def __init__(self, *args):
        self.values = []
        for i in args:
            if isinstance(i, int):
                self.values.append(i)
        self.values.sort()

    def __str__(self):
        if len(self.values) != 0:
            return f'Вектор{tuple(sorted(self.values))}'
        return 'Пустой вектор'

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*map(lambda x: x + other, self.values))
#            return Vector(*[self.values[i] + other for i in range(len(self.values))])
        if isinstance(other, Vector):
            if len(other.values) == len(self.values):
                return Vector(*[self.values[i] + other.values[i] for i in range(len(self.values))])
#            return Vector(*list(map(lambda x, y: x + y, self.values, other.values)))
# print(*map(lambda x: x[0] + x[1], zip(i, j)))
            return 'Сложение векторов разной длины недопустимо'
        print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*map(lambda x: x * other, self.values))
#            return Vector(*[self.values[i] * other for i in range(len(self.values))])
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                return Vector(*[self.values[i] * other.values[i] for i in range(len(self.values))])
#            return Vector(*list(map(lambda x, y: x * y, self.values, other.values)))
            return 'Умножение векторов разной длины недопустимо'
        print(f'Вектор нельзя умножать с {other}')

v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"

v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"
"""

# Магические методы сравнения
# __eq__ ==
# __ne__ !=
# __lt__ <
# __le__ <=
# __gt__ >
# __ge__ >=
"""class Restangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        print('__eq__')
        if isinstance(other, Restangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        print('__lt__')
        if isinstance(other, Restangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other

    def __le__(self, other):
        print('__le__')
        return self == other or self < other"""

"""class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.rating == other
        if isinstance(other, ChessPlayer):
            return self.rating == other.rating
        return 'Невозможно выполнить сравнение'

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.rating > other
        if isinstance(other, ChessPlayer):
            return self.rating > other.rating
        return 'Невозможно выполнить сравнение'

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.rating < other
        if isinstance(other, ChessPlayer):
            return self.rating < other.rating
        return 'Невозможно выполнить сравнение'
"""

# __eq__    __hash__
"""class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point) and self.x == other.x and \
                self.y == other.y:
            return

    def __hash__(self):
        return hash((self.x, self.y))"""

# __bool__
"""class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('__len__')
        return abs(self.x - self.y)

    def __bool__(self):
        print('__bool__')
        return self.x != 0 or self.y != 0"""

"""class City:
    def __init__(self, name):
        self.name = name.title()

    def __str__(self):
        return self.name

    def __bool__(self):
        return self.name[-1] not in ('a', 'e', 'i', 'o', 'u')"""

"""class Quadrilateral:
    def __init__(self, width, height=None):     # хороший способ
        self.width = width
        self.height = height or width

    def __str__(self):
        if self.height == self.width:
            return f'Куб размером {self.width}х{self.width}'
        return f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        return self.width == self.height"""


"""class Decorator:
    def __init__(self, func):
        print('> Класс Decorator метод __init__')
        self.func = func

    def __call__(self):
        print('> перед вызовом класса...', self.func.__name__)
        self.func()
        print('> после вызова класса')

@Decorator
def wrapped():
    print('функция wrapped')

print('>> старт')
wrapped()
print('>> конец')
"""

# Полиморфизм
# Полиморфизм в языках программирования и теории типов —
# способность функции обрабатывать данные разных типов.
"""class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class Square:

    def __init__(self, a):
        self.a = a

    def get_area(self):
        return self.a ** 2


class Circle:

    def __init__(self, r):
        self.r = r

    def get_area(self):
        return 3.14 * self.r**2"""

# __getitem__   __setitem__     __delitem__
# extend
"""class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if isinstance(item, int) and 1 <= item <= len(self.values):
            return self.values[item - 1]
        else:
            raise IndexError('Индекс за границами нашей коллекции или введено не целое число!')

    def __setitem__(self, key, value):
        if isinstance(key, int) and 1 <= key <= len(self.values):
            self.values[key - 1] = value
        elif key>len(self.values):
            diff = key - len(self.values)
            self.values.extend([0] * diff)
            self.values[key - 1] = value
        else:
            raise IndexError('Индекс за границами нашей коллекции или введено не целое число!')

    def __delitem__(self, key):
        if isinstance(key, int) and 1 <= key <= len(self.values):
            del self.values[key - 1]
        else:
            raise IndexError('Индекс за границами нашей коллекции или введено не целое число!')"""

"""class PowTwo:
    def __init__(self, m=0):
        self.m = m

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.m:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration('Больше чем нужно')

for i in PowTwo(10):
    print(i)

c = PowTwo(5)
j = iter(c)
print(next(j))"""

"""class PowTwo:
    def __init__(self, *args):
        self.args = args

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.args):
            self.n += 1
            return self.args[self.n - 1]
        else:
            return 'Конец'

    def __len__(self):
        return len(self.args)

p = PowTwo(12, 26, 3231, 421312, 512531)
i = iter(p)
print(len(p))
print(next(i))"""

# Наследование
# Наследование — концепция объектно-ориентированного программирования,
# согласно которой абстрактный тип данных может
# наследовать данные и функциональность некоторого существующего типа.

"""class Person:   # parent
    def can_breathe(self):
        print('Я могу дышать')

    def can_walk(self):
        print('Я могу ходить')


class Doctor(Person):   # subclass
    def can_Cure(self):
        print('Я могу лечить')


class Ortoped(Doctor):
    pass


class Architect(Person):    # subclass
    def can_build(self):
        print('Я могу строить дома')"""

"""
class Vehicle: pass
class Car(Vehicle): pass
class Plane(Vehicle):pass
class Boat(Vehicle): pass
class RaceCar(Car): pass"""

"""class NewInt(int):
    def repeat(self,n=2):
        return int(str(self) * n)

    def to_bin(self):
        return int(bin(self)[2:])"""


# Переопределение
"""class Person:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        print('Человек дышит')

    def walk(self):
        print('Человек идет')

    def sleep(self):
        print('Human sleeping')

    def combo(self):
        self.breathe()
        self.walk()
        self.sleep()

    def __str__(self):
        return f'Person {self.name}'


class Doctor(Person):

    def breathe(self):
        print('Доктор дышит')

    def __str__(self):
        return f'Doctor {self.name}'"""

# Extend
"""class Person:

    def breathe(self):
        print('Human breathing')

    def sleep(self):
        print('Human sleep')

    def combo(self):
        self.breathe()
        if hasattr(self, 'walk'):
            self.walk()
        self.sleep()


class Doctor(Person):

    def breathe(self):
        print('Doctor breathing')

    def sleep(self):
        print('Doctor sleep')

    def walk(self):
        print('Doctor walk')
"""


# Делегирование, super()
"""class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return  f'Person {self.name} {self.surname}'

    def info(self):
        print('Parent class')
        print(self)

    def breathe(self):
        print('Человек дышит')

class Doctor(Person):
    def __init__(self, name, surname, age):
        #self.name = name
        #self.surname = surname
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return  f'Doctor {self.name} {self.surname}'

    def breathe(self):
        # super().breathe()
        print('Doctor breath')"""


"""class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'{self.__x}, {self.__y}'

class Styles:
    def __init__(self):
        print('Styles')
        super().__init__()

class Pos:
    def __init__(self):
        print('Pos')
        super().__init__()

class Line(Pos, Styles):
    def __init__(self, sp:Point, ep:Point, color='red', width=1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width
        super().__init__()

    def draw(self):
        print(f'Рисование линии :{self._sp}, {self._ep}, {self._color}, {self._width}')"""

"""class Transport:
    def __init__(self, brand, max_speed, kind=None):
        self.brand = brand
        self.max_speed = max_speed
        self.kind = kind

    def __str__(self):
        return f'Тип транспорта {self.kind} марки {self.brand} может развить скорость {self.max_speed} км/ч'

class Car(Transport):
    def __init__(self, brand, max_speed, mileage, gasoline_residue):
        super().__init__(brand, max_speed, kind='Car')
        self.mileage = mileage
        self.__gasoline_residue = gasoline_residue
        
    @property
    def gasoline(self):
        return f'Осталось бензина на {self.__gasoline_residue} км'

    @gasoline.setter
    def gasoline(self, value):
        if isinstance(value, int):
            self.__gasoline_residue += value
            print(f'Объем топлива увеличен на {value} л и составляет {self.__gasoline_residue} л')
            return
        print('Ошибка заправки автомобиля')
        return

class Boat(Transport):
    def __init__(self, brand, max_speed, owners_name):
        super().__init__(brand, max_speed, kind='Boat')
        self.owners_name = owners_name

    def __str__(self):
        return f'Этой лодкой марки {self.brand} владеет {self.owners_name}'

class Plane(Transport):
    def __init__(self,  brand, max_speed, capacity):
        super().__init__(brand, max_speed, kind='Plane')
        self.capacity = capacity

    def __str__(self):
        return f'Самолет марки {self.brand} вмещает в себя {self.capacity} людей'"""

"""class Initialization:
    def __init__(self, capacity, food=[]):
        if isinstance(capacity, int):
            self.capacity = capacity
            self.food = food
        else:
            print('Количество людей должно быть целым числом')

class Vegetarian(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f"{self.capacity} людей предпочитают не есть мясо! Они предпочитают {self.food}"

class MeatEater(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'{self.capacity} мясоедов в Москве! Помимо мяса они едят еще и {self.food}'

class SweetTooth(Initialization):
    def __init__(self, capacity, food):
        super().__init__(capacity, food)

    def __str__(self):
        return f'Сладкоежек в Москве {self.capacity}. Их самая любимая еда: {self.food}'

    def __eq__(self, other):
        if isinstance(other, int):
            return self.capacity == other
        if isinstance(other, (MeatEater, Vegetarian, SweetTooth)):
            return self.capacity == other.capacity
        return f'Невозможно сравнить количество сладкоежек с {other}'

    def __lt__(self, other):
        if isinstance(other, int):
            return self.capacity < other
        if isinstance(other, (MeatEater, Vegetarian, SweetTooth)):
            return self.capacity < other.capacity
        return f'Невозможно сравнить количество сладкоежек с {other}'

    def __gt__(self, other):
        if isinstance(other, int):
            return self.capacity > other
        if isinstance(other, (MeatEater, Vegetarian, SweetTooth)):
            return self.capacity > other.capacity
        return f'Невозможно сравнить количество сладкоежек с {other}'

"""
# ниже функция которая могла бы быть
""" def minimum(self, value, method):
        if isinstance(value, (MeatEater, Vegetarian)):
            return eval(f'{self.capacity} {method} {value.capacity}')
        elif isinstance(value, int):
            return eval(f'{self.capacity} {method} {value}')
        return f'Невозможно сравнить количество сладкоежек с {value}'

    def __eq__(self, other):
        return self.minimum(other, '==')

    def __lt__(self, other):
        return self.minimum(other, '<')

    def __gt__(self, other):
        return self.minimum(other, '>')
    """


# МРО __mro__
"""class Doctor:

    def __init__(self, degree):
        self.degree = degree

    def graduate(self):
        print('Ура я отучился на доктора')

    def can_build(self):
        print('Я доктор, я умею строить')


class Builder:

    def __init__(self, rank):
        self.rank = rank

    def graduate(self):
        print('Ура я отучился на строителя')

    def can_build(self):
        print('Я строитель, я умею строить')


class Person(Doctor, Builder):

    def __init__(self, rank, degree):
        super().__init__(degree)
        Builder.__init__(self, rank)

    def __str__(self):
        return f'Person {self.rank} {self.degree}'"""

# (<class '__main__.Person'>, <class '__main__.Doctor'>, <class '__main__.Builder'>, <class 'object'>)

# В eval() функция оценивает указанный выражение,
# если выражение является допустимым оператором Python, оно будет выполнено.

# __slots__ - занимает меньше места
"""class Dota:
    def __init__(self, rank, hero):
        self.rank = rank
        self.hero = hero

class Fifa:
    def __init__(self, club):
        self.club = club

class Gamer(Dota, Fifa):
    __slots__ = ('rank', 'hero', 'club')
    def __init__(self, rank, hero, club):
        Dota.__init__(self, rank, hero)
        Fifa.__init__(self, club)
    def __str__(self):
        return f'Геймер играет в доту на герое {self.hero} и играет в фифу за {self.club}'
        """


# __slots__ property
"""class Rectangle:
    __slots__ = '__width', 'height'

    def __init__(self, a, b):
        self.width = a
        self.height = b

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value


class Square(Rectangle):
    __slots__ = 'color'

    def __init__(self, a, b, value):
        super().__init__(a, b)
        self.color = value


d = Square(4, 5, 'black')
print(d.width, d.height, d.color)"""

# Exceptions
# try except raise
"""print(1)
try :
    int('Heeli')
except ValueError:
    print('Error, smth incorrect')
print(3)

t = IndexError()
print(isinstance(t, BaseException))
raise ValueError()
"""

# 1
"""class Wallet:
    __slots__ = 'currency', 'balance'

    def __init__(self, txt, balance):
        if type(txt) != str :
            raise TypeError('Неверный тип валюты')
        else:
            if len(txt) != 3:
                raise NameError('Неверная длина названия валюты')
            else:
                if txt != txt.upper():
                    raise ValueError("Название должно состоять только из заглавных букв")
                else:
                    self.currency = txt
                    self.balance = balance

    def __eq__(self, other):
        if type(other) != type(self):
            raise TypeError(f'Wallet не поддерживает сравнение с {other}')
        else:
            if self.currency != other.currency:
                raise ValueError("Нельзя сравнить разные валюты")
            else:
                return self.balance == other.balance

    def __add__(self, other):
        if isinstance(other, Wallet) and self.currency == other.currency:
            return Wallet(self.currency, self.balance + other.balance)
        else:
            raise ValueError("Данная операция запрещена")

    def __sub__(self, other):
        if isinstance(other, Wallet) and self.currency == other.currency:
            return Wallet(self.currency, self.balance - other.balance)
        else:
            raise ValueError("Данная операция запрещена")
"""
# 2
"""class Wallet:
    def __init__(self, currency, balance):
        if not isinstance(currency, str):
            raise TypeError('Неверный тип валюты')
        elif isinstance(currency, str) and len(currency) != 3:
            raise NameError('Неверная длина названия валюты')
        elif currency != currency.upper():
            raise ValueError('Название должно состоять только из заглавных букв')
        self.currency = currency
        self.balance = balance

    def __eq__(self, other):
        if not isinstance(other, Wallet):
            raise TypeError(f'Wallet не поддерживает сравнение с {other}')
        elif self.currency != other.currency:
            raise ValueError('Нельзя сравнить разные валюты')
        return self.balance == other.balance

    def __add__(self, other):
        if isinstance(other, Wallet) and self.currency == other.currency:
            return Wallet(self.currency, self.balance + other.balance)
        raise ValueError('Данная операция запрещена')

    def __sub__(self, other):
        if isinstance(other, Wallet) and self.currency == other.currency:
            return Wallet(self.currency, self.balance - other.balance)
        raise ValueError('Данная операция запрещена')"""

# finally   else
"""s = 'hello'
d = {}
try:
    d['key']
    s[6]
except (KeyError, IndexError):  # except можешь быть сколько угодно
    print('error')
except ZeroDivisionError:
    print('error')
else:   # работает только если нет исключения
    print('good')
finally:    # работает всегда
    print('Sonya loh')"""

"""try:
    raise ValueError('Ошибка значения')
except ValueError as first:
    try:
        raise TypeError('Ошибка типа')
    except TypeError as second:
        raise Exception('Большое исключение') from first"""

# Custom Exception Python
"""def exception_raiser(string):
    if isinstance(string, int):
        raise ValueError
    elif isinstance(string, str):
        raise IndexError
    else:
        raise TypeError"""