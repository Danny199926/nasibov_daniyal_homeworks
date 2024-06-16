# Создайте класс Students, содержащий поля:
# фамилия и инициалы,
# номер группы,
# успеваемость (список из пяти элементов).
#
# Создать класс School:
#
# Добавить возможность для добавления студентов в школу
#
# Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 5 или 6.
#
# Добавить возможность вывода учеников заданной группы
#
# Добавить возможность вывода учеников претендующих на автомат(средний балл >= 7)

class Students:
    def __init__(self, surname_and_initials, number_of_group, progress):
        self.surname_and_initials = surname_and_initials
        self.number_of_group = number_of_group
        self.progress = progress


class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def print_excellent_students(self):
        for student in self.students:
            if all(mark == 5 or mark == 6 for mark in student.progress):
                print(f'Студент {student.surname_and_initials} группы No {student.number_of_group}, имеет оценки 5 и 6')

    def print_students_of_group(self, number_of_group):
        for student in self.students:
            if student.number_of_group == number_of_group:
                print(f'Студент группы {number_of_group}: {student.surname_and_initials}')

    def automatic_pass(self):
        for student in self.students:
            if (sum(student.progress) / len(student.progress)) >= 7:
                print(f'Студент {student.surname_and_initials} получает автомат')


school = School()
student1 = Students('Иванов А.А.', 1, (5, 5, 6, 5, 5))
student2 = Students('Кузнецов В.В.', 2, (8, 9, 6, 5, 10))
student3 = Students('Антонов М.Н.', 1, (3, 4, 2, 3, 6))
student4 = Students('Ермолова Т.П.', 2, (9, 4, 5, 7, 4))
school.add_student(student1)
school.add_student(student2)
school.add_student(student3)
school.add_student(student4)

school.print_excellent_students()
number_of_group = int(input('Введите номер группы: '))
school.print_students_of_group(number_of_group)
school.automatic_pass()
