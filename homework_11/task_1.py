# Создайте функцию для определения наибольшего числа
import random


def max_of_num(*args):
    for nums in args:
        print(max(nums))


nums = [random.randint(1, 100) for i in range(10)]
print(nums)
max_of_num(nums)