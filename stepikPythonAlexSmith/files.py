# fw = open('doc/file.txt', 'a')
# fw.write('Hello world\n')
# fw.close()

# var = input('Type something: ')
# fw_2 = open('doc/file2.txt', 'a')
# fw_2.write(var)
# fw_2.close()

# a - запись новых данных и их размещение в конец файла
# w - запись новых данных, но удаление старых
# r - чтение данных

fw = open('doc/file3.txt', 'w')
fw.write('Hi\n')
fw.close()

fr = open('doc/file.txt', 'r')
first_line = fr.readline()  # читаем только первую строку
lines = fr.readlines()  # читаем несколько строк
content = fr.read()  # читаем всё
for i in range(len(lines)):
    print(lines[i].strip())  # strip удалит символы новой строки
fw.close()
print(first_line)
print(content)

films = 'Матрица Скала Схватка Бэтман'.split()
fw = open('doc/fileX.txt', 'w')
for f in films:
    fw.write(f'{f}\n')
fw.close()

fr = open('doc/fileX.txt', 'r')
lines = fr.readlines()
for i in range(len(lines)):
    print(lines[i].strip())
    if i + 1 < len(lines):
        print('*****')
fw.close()
