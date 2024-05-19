# 7.Дан список [student1, student2, student3] с помощью цикла for добавить к каждому элементу списка слово “_good”.
# Вывести на экран.
students = ['student1', 'student2', 'student3']
for i in range(len(students)):
    students[i] += '_good'
print(students)