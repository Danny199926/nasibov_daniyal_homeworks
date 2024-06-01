import os

os.rename('task2.txt', 'text_file.txt')
os.replace('text_file.txt', r'C:\Users\User\PycharmProjects\homework_13\new_directory\test.path.txt')
print(f' путь текущей дериктории {os.getcwd()}')
os.chdir('..')
print(f' путь текущей дериктории {os.getcwd()}')
os.remove(r'C:\Users\User\PycharmProjects\homework_13\task1.txt')
os.mkdir('folder1')
os.makedirs('folder2/folder3/folder4')
os.rmdir('folder1')
os.removedirs('folder2/folder3/folder4')
os.mkdir('folder1')
os.rmdir('folder1')