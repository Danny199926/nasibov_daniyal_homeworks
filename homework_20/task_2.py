# Создать таблицу в Базе Данных с тремя колонками(id, 2 - text, 3 - text).
# Заполнить её с помощью INSERT данными (3 записи).
# Удалить с помощью DELETE 2 запись. Обновить значения 3-ей записи на:
# hello world с помощью UPDATE
# *Записать данные с таблицы в файл в три колонки. Первая – id, вторая и третья с данными.

import sqlalchemy as db

meta = db.MetaData()

user = db.Table(
    'User', meta,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('col1', db.String(150), nullable=False),
    db.Column('col2', db.String(150), nullable=False)
)
print(user.c)

engine = db.create_engine('mysql+mysqlconnector://name:passwordx@localhost:3306/my_data')
meta.create_all(engine)
connection = engine.connect()

add_query = user.insert().values(col1='data1', col2='data2')
connection.execute(add_query)
connection.commit()
select = db.select(user)
print(connection.execute(select).fetchall())

delete_query_with_id2 = user.delete().where(user.c.id == '3')
result = connection.execute(delete_query_with_id2)
connection.commit()
select = db.select(user)
print(connection.execute(select).fetchall())

update_query = user.update().values(col1='hello', col2='world').where(user.c.id == 5)
connection.execute(update_query)
connection.commit()
select = db.select(user)
print(connection.execute(select).fetchall())
