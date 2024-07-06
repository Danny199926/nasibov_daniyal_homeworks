# поработать с dbeaver
#
# Решить данные задачи при помощи SQL запросов, а также с использования SQLAlchemy
#
# 1) первая задача из класса
# Создайте новую Базу данных.
# В ней создайте таблицу с тремя полями, два текстовых, одно - целое число.
# Число запрашивается с клавиатуры, а слова задаются статически.
# * Выведите каждую запись в отдельную строку
# пример
# [(hello, world, 2), (hello2, world2, 3)]
# Результат работы нашей программы
# hello, world, 2
# hello2, world2, 3

import sqlalchemy as db

meta = db.MetaData()

user = db.Table(
    'mytab', meta,
    db.Column('str1', db.String(155), nullable=False),
    db.Column('str2', db.String(155), nullable=False),
    db.Column('id', db.Integer, primary_key=True)
)
print(user.c)

engine = db.create_engine('mysql+mysqlconnector://name:password@localhost:3306/my_db')
meta.create_all(engine)
connection = engine.connect()
select = db.select(user)
print(connection.execute(select).fetchall())
connection.close()


