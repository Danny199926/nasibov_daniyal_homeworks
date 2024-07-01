# Требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник.
# Для этого создайте класс TriangleChecker, принимающий только положительные числа.
# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
# Ура, можно построить треугольник!
# С отрицательными числами ничего не выйдет!
# Жаль, но из этого треугольник не сделать!

class TriangleChecker:
    def __init__(self, a, b, c):
        if not all(isinstance(x, int) and x > 0 for x in (a, b, c)):
            raise ValueError("С отрицательными числами ничего не выйдет!")
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return "Ура, можно построить треугольник!"
        else:
            return "Жаль, но из этого треугольник не сделать."


try:
    triangle1 = TriangleChecker(3, 4, 5)
    print(triangle1.is_triangle())

    triangle2 = TriangleChecker(1, 2, 5)
    print(triangle2.is_triangle())

    triangle3 = TriangleChecker(-1, 2, 3)
except ValueError as e:
    print(e)


# Задача
# Есть Помидор со следующими характеристиками:
# Индекс
# Стадия зрелости(стадии: Отсутствует, Цветение, Зеленый, Красный)
# Помидор может:
# Расти (переходить на следующую стадию созревания)
# Предоставлять информацию о своей зрелости
# Есть Куст с помидорами, который:
# Содержит список томатов, которые на ней растут
# И может:
# Расти вместе с томатами
# Предоставлять информацию о зрелости всех томатов
# Предоставлять урожай
# И также есть Садовник, который имеет:
# Имя
# Растение, за которым он ухаживает
# И может:
# Ухаживать за растением
# Собирать с него урожай
# Задание:
# Класс Tomato
# Создайте класс Tomato
# Создайте статический атрибут states, который будет содержать все стадии созревания помидора
# Создайте метод __init__(), внутри которого будут определены два приватных атрибута:
# 1) _index - передается параметром и 2) _state - принимает первое значение из словаря states
# Создайте метод grow(), который будет переводить томат на следующую стадию созревания
# Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)
# Класс TomatoBush
# Создайте класс TomatoBush
# Определите метод __init__(), который будет принимать в качестве параметра количество томатов
# и на его основе будет создавать список объектов класса Tomato. Данный список будет храниться внутри атрибута tomatoes.
# Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания
# Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
# Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая
# Класс Gardener
# Создайте класс Gardener
# Создайте метод __init__(), внутри которого будут определены два атрибута:
# 1) name - передается параметром, является публичным и 2) _plant - принимает объект класса TomatoBush,
# является приватным
# Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
# Создайте метод harvest(), который проверяет, все ли плоды созрели.
# Если все - садовник собирает урожай. Если нет - метод печатает предупреждение.
# Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.
# Тесты (main)
# Вызовите справку по садоводству
# Создайте объекты классов TomatoBush и Gardener
# Используя объект класса Gardener, поухаживайте за кустом с помидорами
# Попробуйте собрать урожай
# Если томаты еще не дозрели, продолжайте ухаживать за ними
# Соберите урожай

class Tomato:
    states = {'Отсутствует': 0, 'Цветение': 1, 'Зеленый': 2, 'Красный': 3}

    def __init__(self, index):
        self.__index = index
        self.__state = self.states['Отсутствует']

    def grow(self):
        if self.__state < 3:
            self.__state += 1

    def is_ripe(self):
        if self.__state == 3:
            return True
        else:
            return False


class TomatoBush:

    def __init__(self, count):
        self.tomatoes = [Tomato(index) for index in range(1, count + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self.__plant = plant

    def work(self):
        self.__plant.grow_all()

    def harvest(self):
        if self.__plant.all_are_ripe():
            print('Урожай собран!')
            self.__plant.give_away_all()
        else:
            print('Томаты еще не созрели')

    @staticmethod
    def knowledge_base():
        print('Справка по садоводству:')
        print('1. Не забывайте регулярно поливать и подкармливать растения')
        print('2. Определите правильное расстояние между растениями, чтобы они не мешали друг другу в росте')
        print('3. Удалите поврежденные листья и плоды, чтобы предотвратить распространение болезней')


Gardener.knowledge_base()

bush = TomatoBush(4)
gardener = Gardener('Jack', bush)
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()

# Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age.
# По умолчанию name = Ivan, age = 18, groupNumber = 10A. Необходимо создать пять методов: getName, getAge,
# getGroupNumber, setNameAge, setGroupNumber. Метод getName нужен для получения данных об имени конкретного студента,
# метод getAge нужен для получения данных о возрасте конкретного студента,
# метод setGroupNumber нужен для получения данных о номере группы конкретного студента.
# Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию,
# метод setGroupNumber позволяет изменить номер группы установленный по умолчанию.
# В программе необходимо создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы.
class Student:
    def __init__(self, name='Ivan', age='18', groupNumber='10A'):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getGroupNumber(self):
        return self.groupNumber

    def setNameAge(self):
        self.name = self.name
        self.age = self.age
        return f'Имя студента {self.name}, возраст студента {self.age}'

    def setGroupNumber(self):
        self.groupNumber = self.groupNumber
        return f'Группа студента {self.groupNumber}'


student = Student('Александр', '17', '10B')
student2 = Student('Михаил', '16', '10E')
student3 = Student('Кристина', '15', '10A')
student4 = Student('Максим', '19', '11B')
student5 = Student('Екатерина', '17', '11G')
print(student.setNameAge(), student.setGroupNumber())
print(student2.setNameAge(), student2.setGroupNumber())
print(student3.setNameAge(), student3.setGroupNumber())
print(student4.setNameAge(), student4.setGroupNumber())
print(student5.setNameAge(), student5.setGroupNumber())


# Класс «Волшебник» (Wizard)
# Экземпляр класса при инициализации принимает аргументы:
# – имя;
# – рейтинг;
# – на какой возраст выглядит.
# Класс должен обеспечивать функциональность:
# – change_rating(value) – изменять рейтинг на значение value; не может стать больше 100 и
# меньше 1, изменяется только до достижения экстремального значения; при увеличении
# рейтинга уменьшается возраст на abs(value) // 10, но только до 18, дальше не уменьшается;
# при уменьшении рейтинга возраст соответственно увеличивается;
# – к экземпляру класса можно прибавить строку: (wd += string), значение рейтинга
# увеличивается на ее длину, а возраст, соответственно, уменьшается на длину // 10, условия
# изменения такие же;
# – экземпляр класса можно вызвать с аргументом-числом; возвращает значение: (аргумент
# - возраст) * рейтинг;
# __str__() – возвращает строку:
# “Wizard <name> with <rating> rating looks <age> years old”
# – экземпляры класса можно сравнивать: сначала по рейтингу, затем по возрасту, затем по
# имени по алфавиту; для этого нужно реализовать методы сравнения: <, >, <=, >=, ==, !=.
class Wizard:
    def __init__(self, name, rating, age):
        self.name = name
        self.rating = rating
        self.age = age

    def change_rating(self, value):
        if self.rating + value < 100:
            self.rating += value
            if self.age > 18:
                self.age = abs(value) // 10
            else:
                self.age = 18
        elif self.rating - value > 1:
            self.rating -= value
            self.age = abs(value) * 10
        else:
            ValueError('Вы достигли экстремального значения')

    def __add__(self, string):
        if self.rating + len(string) < 100:
            self.rating += len(string)
            if self.age > 18:
                self.age = len(string) // 10
            else:
                self.age = 18
        else:
            ValueError('Вы достигли экстремального значения')

    def __call__(self, argument):
        return (argument - self.age) * self.rating

    def __str__(self):
        return f'Wizard {self.name} with {self.rating} rating looks {self.age} years old'

    def __lt__(self, other):
        return (self.rating, self.age, self.name) < (other.rating, other.age, other.name)


wd = Wizard("Gideon", 37, 20)
wd.change_rating(10)
print(wd)
wd + 'hello'
print(wd)
print(wd(50))

wd2 = Wizard("Lucius", 64, 18)
wd3 = Wizard("Merlin", 99, 25)
print(wd2 < wd3, wd2 > wd3)
print(wd2, wd3, sep='\n')


#  Класс «Сотрудник компании» Worker
# Экземпляр класса при инициализации принимает аргументы: имя,
# должность и стаж работы сотрудника, метод print_info() выводит информацию о сотруднике в формате:
# «Имя: Василий Должность: Системный администратор :Стаж: 3 года» При выводе стажа нужно учитывать,
# что «года» должно заменяться на «лет» или «год» в зависимости от числа.
# worker1 = Worker("Алексей", "Программист", 17)
#  worker1.print_info()
# worker2 = Worker("Анна", "Маркетолог", 2)
# worker2.print_info()
# worker3 = Worker("Дмитрий", "Аналитик", 1)
# worker3.print_info()

class Worker:
    def __init__(self, name, position, experience):
        self.name = name
        self.position = position
        self.experience = experience

    def print_info(self):
        if self.experience == 1:
            experience_text = 'год'
        elif 2 <= self.experience <= 4:
            experience_text = 'года'
        else:
            experience_text = 'лет'
        print(f'Имя: {self.name}, должность: {self.position}, стаж работы: {self.experience} {experience_text}')


worker1 = Worker("Алексей", "Программист", 17)
worker1.print_info()
worker2 = Worker("Анна", "Маркетолог", 2)
worker2.print_info()
worker3 = Worker("Дмитрий", "Аналитик", 1)
worker3.print_info()

# Класс ПЕРСОНА, экземпляр класса инициализируется аргументами фамилия, дата
# рождения и содержит методы, позволяющие вывести информацию о персоне, а также определить ее возраст.
# Дочерние классы: АБИТУРИЕНТ (фамилия, дата рождения, факультет),
# СТУДЕНТ(фамилия, дата рождения, факультет, курс), ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность, стаж),
# содержат свои методы вывода информации.
# Создайте список из n персон, выведите полную информацию из базы, а также
# организуйте поиск персон, чей возраст попадает в заданный диапазон.

import datetime


class Person:
    def __init__(self, surname, birth_date):
        self.surname = surname
        self.birth_date = birth_date

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.birth_date.year
        if today.month < self.birth_date.month or (
                today.month == self.birth_date.month and today.day < self.birth_date.day):
            age -= 1
        return age

    def print_info(self):
        print(
            f'Фамилия: {self.surname}, дата рождения: {self.birth_date.strftime('%d.%m.%Y')}, Возраст: {self.get_age()} лет')


class Applicant(Person):
    def __init__(self, surname, birth_date, faculty):
        super().__init__(surname, birth_date)
        self.faculty = faculty

    def print_info(self):
        print(
            f'Фамилия: {self.surname}, дата рождения: {self.birth_date.strftime('%d.%m.%Y')}, Возраст: {self.get_age()} лет, Факультет: {self.faculty}')


class Student(Person):
    def __init__(self, surname, birth_date, faculty, course):
        super().__init__(surname, birth_date)
        self.faculty = faculty
        self.course = course

    def print_info(self):
        print(
            f'Фамилия: {self.surname}, дата рождения: {self.birth_date.strftime('%d.%m.%Y')}, Возраст: {self.get_age()} лет, Факультет: {self.faculty}, Курс: {self.course}')


class Teacher(Person):
    def __init__(self, surname, birth_date, faculty, position, experience):
        super().__init__(surname, birth_date)
        self.faculty = faculty
        self.position = position
        self.experience = experience

    def print_info(self):
        print(
            f'Фамилия: {self.surname}, дата рождения: {self.birth_date.strftime('%d.%m.%Y')}, Возраст: {self.get_age()} лет, Факультет: {self.faculty}, Должность: {self.position}, Стаж: {self.experience}')


persons = [
    Applicant("Иванов", datetime.date(1998, 6, 25), "Математика"),
    Student("Петрова", datetime.date(2000, 5, 2), "Физика", 3),
    Teacher("Сидоров", datetime.date(1975, 12, 8), "История", "Профессор", 20),
    Person("Васильева", datetime.date(1985, 9, 1))
]

print('Полная информация о персонах')
for person in persons:
    person.print_info()

min_age = 20
max_age = 30
print(f"\nПерсоны в возрасте от {min_age} до {max_age} лет:")
for person in persons:
    if min_age <= person.get_age() <= max_age:
        person.print_info()


