# Класс Post описывает публикацию от пользователя в сети:
# – никнейм пользователя,
# – время публикации,
# – количество лайков,
# – текст сообщения,
# – список комментариев.
# Конструктор класса получает автора, устанавливает время, а для комментариев создает списочный массив.
# Добавить метод, позволяющий поставить лайк сообщению.
import datetime


class Post:

    def __init__(self, author, text):
        self.author = author
        self.time = datetime.datetime.now()
        self.likes = 0
        self.text = text
        self.comments = []

    def add_likes(self):
        self.likes += 1

    def add_comments(self, comment):
        self.comments.append(comment)


input_message = input('Enter message: ')
post = Post('Danny1999', input_message)
post.add_likes()
add_comment = input('Enter comment: ')
post.add_comments(add_comment)
print(f'author: {post.author}')
print(f'time {post.time}')
print(f'likes: {post.likes}')
print(f'message: {post.text}')
print(f'comment: {post.comments}')


# Экземпляр класса инициализируется с аргументом name – именем котенка. Класс
# реализует методы:
# – to_answer() – ответить: котенок через один раз отвечает да или нет, начинает с да. Метод
# возвращает “moore-moore”, если да, “meow-meow”, если нет. Одновременно
# увеличивается количество соответствующих ответов;
# – number_yes() – количество ответов да;
# – number_no() – количество ответов нет.
# Пример 1
# Ввод:
# tk = Talking('Pussy')
# print(tk.to_answer())
# print(tk.to_answer())
# print(tk.to_answer())
# print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')
# Вывод:
# moore-moore
# meow-meow
# moore-moore
# Pussy says "yes" 2 times, "no" 1 times

class Talking:

    def __init__(self, name):
        self.name = name
        self.yes_count = 0
        self.no_count = 0
        self.answer = True

    def to_answer(self):
        if self.answer:
            self.yes_count += 1
            self.answer = False
            return 'moore-moore'
        else:
            self.no_count += 1
            self.answer = True
            return 'meow-meow'

    def number_yes(self):
        return self.yes_count

    def number_no(self):
        return self.no_count


tk = Talking('Pussy')
print(tk.to_answer())
print(tk.to_answer())
print(tk.to_answer())
print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')


# Экземпляру класса при инициализации передается аргумент – список тем для
# разговора.
# Класс реализует методы:
# – add_theme(value) – добавить тему в конец;
# – shift_one() – сдвинуть темы на одну вправо (последняя становится первой, остальные
# сдвигаются);
# – reverse_order() – поменять порядок тем на обратный;
# – get_themes() – возвращает список тем;
# – get_first() – возвращает первую тему.
# Пример 1
# Ввод:
# tl = Themes(['weather', 'rain'])
# tl.add_theme('warm')
# print(tl.get_themes())
# tl.shift_one()
# print(tl.get_first())
# Вывод:
# ('weather', 'rain', 'warm')
# warm

class Themes:

    def __init__(self, themes):
        self.themes = themes

    def add_theme(self, value):
        self.themes.append(value)

    def shift_one(self):
        self.themes.insert(0, self.themes.pop())

    def reverse_order(self):
        self.themes.reverse()

    def get_themes(self):
        return tuple(self.themes)

    def get_first(self):
        return self.themes[0]


tl = Themes(['weather', 'rain'])
tl.add_theme('warm')
print(tl.get_themes())
tl.shift_one()
print(tl.get_first())

# Класс Bus содержит свойства:
# – speed (скорость),
# –capacity (максимальное количество пассажиров),
# – maxSpeed (максимальная скорость),
# – passengers (список имен пассажиров),
# – hasEmptySeats (наличие свободных мест),
# – seats (словарь мест в автобусе);
# методы:
# – посадка и высадка одного или нескольких пассажиров,
# – увеличение и уменьшение скорости на заданное значение.
# – операции "in", "+=" и "−=" (посадка и высадка пассажира(ов) с заданной фамилией)

class Bus:
    def __init__(self, speed, capacity, max_speed):
        self.speed = speed
        self.capacity = capacity
        self.max_speed = max_speed
        self.passengers = []
        self.seats = {i: None for i in range(1, capacity + 1)}

    def embark(self, *names):
        for name in names:
            if len(self.passengers) < self.capacity:
                self.passengers.append(name)
                empty_seat = next(seat for seat, occupant in self.seats.items() if occupant is None)
                self.seats[empty_seat] = name
                print(f"{name} сел в автобус на место {empty_seat}")
            else:
                print("Автобус полон!")

    def disembark(self, *names):
        for name in names:
            if name in self.passengers:
                self.passengers.remove(name)
                seat = next(seat for seat, occupant in self.seats.items() if occupant == name)
                self.seats[seat] = None
                print(f"{name} вышел из автобуса с места {seat}")
            else:
                print(f"{name} не находится в автобусе!")

    def increase_speed(self, value):
        if self.speed + value <= self.max_speed:
            self.speed += value
            print(f"Скорость увеличена на {value} км/ч и составляет теперь {self.speed} км/ч")
        else:
            print("Превышена максимальная скорость!")

    def decrease_speed(self, value):
        if self.speed - value >= 0:
            self.speed -= value
            print(f"Скорость уменьшена на {value} км/ч и составляет теперь {self.speed} км/ч")
        else:
            print("Скорость не может быть отрицательной!")

    def __contains__(self, name):
        return name in self.passengers

    def __iadd__(self, name):
        self.embark(name)
        return self

    def __isub__(self, name):
        self.disembark(name)
        return self


bus = Bus(speed=0, capacity=50, max_speed=60)
bus += "Иван"
bus += "Мария"
bus += "Петр"
print("Пассажиры в автобусе:", bus.passengers)
print("Свободные места в автобусе:", [seat for seat, occupant in bus.seats.items() if occupant is None])
bus -= "Иван"
print("Пассажиры в автобусе:", bus.passengers)
print("Свободные места в автобусе:", [seat for seat, occupant in bus.seats.items() if occupant is None])
bus.increase_speed(40)
bus.decrease_speed(20)