#  Создайте класс Робот
#
#  создайте 2 типа оружия: меч, автомат
#
#  Создайте 2 типа амуниции: броня, шлем
#
#  Добавьте оружию и амуниции свои характеристики(например урон, прочность)
#
#  Создайте своего робота с каким либо оружием
#
#  (может быть несколько и брони может быть несколько. Так же может быть ничего)
#
#  Выведите весь арсенал робота на экран

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return f'{self.name}, (урон: {self.damage})'


class Armor:
    def __init__(self, name, durability):
        self.name = name
        self.durability = durability

    def __str__(self):
        return f'{self.name}, (прочность: {self.durability}'


class Robot:
    def __init__(self, name):
        self.name = name
        self.weapons = []
        self.armor = []

    def add_weapon(self, weapon):
        self.weapons.append(weapon)

    def add_armor(self, armor):
        self.armor.append(armor)

    def display_arsenal(self):
        print(f'арсенал робота {self.name}')
        if self.weapons:
            print("Оружие:")
            for weapon in self.weapons:
                print(weapon)
        else:
            print("Оружия нет")
        if self.armor:
            print("Броня:")
            for armor in self.armor:
                print(armor)
        else:
            print("Брони нет")


weapon1 = Weapon('Меч', 15)
weapon2 = Weapon('AK-47', 10)

armor1 = Armor('Тяжелая броня', 50)
armor2 = Armor('Стальной шлем', 20)

robot = Robot('DN-26')
robot.add_armor(armor1)
robot.add_armor(armor2)
robot.add_weapon(weapon1)
robot.add_weapon(weapon2)

robot.display_arsenal()

