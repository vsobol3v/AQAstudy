file_name = 'doc/file.txt'
data = 'Hello world'

# fw = open(file_name, 'a')
# fw.write(data)
# fw.close()

with open(file_name, 'a') as files:
    files.write(f'\n{data}')

# Использование with для работы с файлами имеет несколько преимуществ:
# 1. Автоматическое закрытие файла: После выхода из блока with файл автоматически закрывается, даже если произошло
# исключение. Это помогает избежать утечек ресурсов и гарантирует, что файл всегда будет корректно закрыт.
# 2. Более чистый и компактный код: Использование with делает код более читабельным и компактным, так как нет
# необходимости вручную вызывать метод close() для закрытия файла.

films = 'Матрица Скала Западня Бэтман'.split()
file_1 = 'doc/fileX1.txt'
with open(file_name, 'w', encoding='utf-8') as files:
    for n in films:
        files.write(f'{n}\n')

with open(file_name, 'r', encoding='utf-8') as files:
    lines = files.readlines()
    lines.sort()
    for i in range(len(lines)):
        print(lines[i].strip())