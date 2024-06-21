class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return self.age + self.name

    def __str__(self):
        return self.name


cat = Cat('Kitty', 2)
print(cat)
