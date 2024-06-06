# Напишите программу, которая запрашивает у пользователя данные о студентах и сохраняет
# их в файл формата CSV.
# Требования:
# Программа должна запрашивать у пользователя информацию о каждом студенте, включая имя, фамилию и возраст.
# Информация о каждом студенте должна быть сохранена в отдельной строке файла CSV.
# Файл CSV должен иметь следующие заголовки столбцов: "Имя", "Фамилия", "Возраст".
# Программа должна продолжать запрашивать информацию о студентах до тех пор, пока пользователь
# не введет команду "stop" для завершения.
# В конце выполнения программы должно быть выведено сообщение о успешном сохранении данных.
import csv


def data_students():
    students = []
    while True:
        name_student = input('Введите имя студента: ')
        if name_student.lower() == 'stop':
            break
        lastname_student = input('Введите фамилию студента: ')
        if lastname_student.lower() == 'stop':
            break
        age = input('Введите возраст студента: ')
        if age.lower() == 'stop':
            break
        students.append([name_student, lastname_student, age])
    return students


with open('class_task.csv', 'w', encoding='cp1251', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(('Имя', 'Фамилия', 'Возраст'))
    writer.writerows(data_students())
print('Данные успешно сохранены')