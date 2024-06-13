class Human:
    distance = int(input('Введите дистанцию для заплыва в метрах: '))

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self, km):
        if km <= 5:
            return f'{self.name} может пройти {km} км'
        else:
            return f'{self.name} не может пройти {km} км'

    def swim(self):
        if self.distance <= 30:
            return f'{self.name} может проплыть {self.distance} метров'
        else:
            return f'{self.name} не может проплыть {self.distance} метров'


my_human = Human('Danny', 25)
input_count_km = int(input('Введите кол-во км, которое должен пройти Danny: '))
print(my_human.walk(input_count_km))
print(my_human.swim())
