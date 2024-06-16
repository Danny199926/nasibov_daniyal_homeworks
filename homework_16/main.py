# Представление объектов
class Human:
    def __str__(self):
        return f'object class human'

    def __repr__(self):
        return f'object class human for def'


human = Human()
print(human)


# Декораторы classmethod и staticmethod
class Human:
    @classmethod
    def class_method_human(cls):
        return 'Это метод класса'

    @staticmethod
    def func_in_class():
        return 'Эта функция внутри класса'


print(Human.class_method_human())
print(Human.func_in_class())


# Функция super()
class Base:

    def price(self):
        return 10


class InterFoo(Base):

    def price(self):
        return super().price() * 1.1


class NewClass(InterFoo):

    def price(self):
        return super().price() * 0.8


x = InterFoo()
print(x.price())
y = NewClass()
print(y.price())


class Class1:

    def __init__(self, atr1, atr2):
        self.atr1 = atr1
        self.atr2 = atr2


class Class2(Class1):

    def __init__(self, atr1, atr2, atr3, atr4):
        super().__init__(atr1, atr2)
        self.atr3 = atr3
        self.atr4 = atr4


val1 = Class1(1, 2)
val2 = Class2(1, 2, 3, 4)
print(val1.atr1, val2.atr2)
print(val2.atr1, val2.atr2, val2.atr3, val2.atr4)

# Абстракция
from abc import ABC, abstractmethod


class Book(ABC):

    def __init__(self, name, author):
        self.name = name
        self.author = author

    @abstractmethod
    def get_info_of_book(self):
        pass


class Detective(Book):

    def get_info_of_book(self):
        return f'Эта книга жанра детектив, название {self.name}, автор {self.author}'


class Fantasy(Book):

    def get_info_of_book(self):
        return f'Эта книга жанра фэнтази, название {self.name}, автор {self.author}'


detective = Detective('Шерлок Холмс', 'Доил')
print(detective.get_info_of_book())
fantasy = Fantasy('Ведьмак', 'Сапковский')
print(fantasy.get_info_of_book())
