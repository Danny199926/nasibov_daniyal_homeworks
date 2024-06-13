# Вы идете в путешествие, надо подсчитать сколько у денег у каждого студента.
# Класс студен описан следующим образом:
#
# class Student:
#     def __init__(self, name, money):
#        self.name = name
#        self.money = money

class Student:
    def __init__(self, name, money):
        self.name = name
        self.money = money


students = [
    Student('Danny', 500),
    Student('Vika', 1000),
    Student('Varvara', 800),
    Student('Kirill', 600)

]
for student in students:
    print(f'У студента {student.name}, {student.money} рублей')
