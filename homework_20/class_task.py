# Создайте новую Базу данных.
# В ней создайте таблицу с тремя полями, два текстовых, одно - целое число.
# Число запрашивается с клавиатуры, а слова задаются статически.
# * Выведите каждую запись в отдельную строку

import mysql.connector

db_connection = mysql.connector.connect(
    host='localhost',
    user='name',
    password='password',
    database='my_database'
)

cursor = db_connection.cursor()

cursor.execute('''CREATE DATABASE IF NOT EXISTS my_database''')
cursor.execute('''USE my_database''')

cursor.execute('''CREATE TABLE IF NOT EXISTS new_table(id INT AUTO_INCREMENT PRIMARY KEY,
text1 VARCHAR(225),
text2 VARCHAR(255),
number INT)''')

input_number = int(input('Введите число: '))
static_text1 = 'ExampleText1'
static_text2 = 'ExampleText2'

cursor.execute('''INSERT INTO new_table (text1, text2, number) VALUES (%s, %s, %s);''',
               (static_text1, static_text2, input_number))

db_connection.commit()

cursor.execute('''SELECT * FROM new_table''')
result = cursor.fetchall()
for row in result:
    print(row)

cursor.close()
db_connection.close()

