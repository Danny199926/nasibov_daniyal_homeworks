# Создать 4 фрукта.
# Апельсин, яблоко, мандарин, банан
# У всех фруктов есть сорт, список витаминов, цена, имя
# У апельсина, мандарина, банана есть метод очистить
# У яблока метод порезать
# У банана есть характеристика: кол-во калия
# Создать 4 объекта фрукта и использовать все доступные методы и характеристики
# При вызове метода очистить, должно писаться имя фрукта
# Например:
# `apple = Apple("sort", [a,b,c], 120, "apple")`
#
# `apple.clear()`
#
# `>>"apple очищен"`

class Fruits:
    def __init__(self, sort, vitamins, price, name):
        self.sort = sort
        self.vitamins = vitamins
        self.price = price
        self.name = name


class Orange(Fruits):
    def clean(self):
        print(f'{self.name}, очищен')


class Mandarin(Fruits):
    def clean(self):
        print(f'{self.name}, очищен')


class Banana(Fruits):
    def __init__(self, sort, vitamins, price, name, potassium):
        super().__init__(sort, vitamins, price, name)
        self.potassium = potassium

    def clean(self):
        print(f'{self.name}, очищен')


class Apple(Fruits):
    def cut(self):
        print(f'{self.name}, порезано')


orange = Orange('Valencia', ['d', 'e', 'f'], 200, 'orange')
mandarin = Mandarin('Klementin', ['g', 'h', 'i'], 300, 'mandarin')
banana = Banana('Cavendish', ['j', 'k', 'l'], 300, 'banana', 420)
apple = Apple('Gala', ['a', 'b', 'c'], 100, 'apple')

orange.clean()
apple.cut()
mandarin.clean()
banana.clean()
print(f"Количество калия в банане: {banana.potassium}")
