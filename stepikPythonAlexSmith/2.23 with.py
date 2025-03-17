file_name = 'doc/file.txt'
data = 'Hello world'

# fw = open(file_name, 'a')
# fw.write(data)
# fw.close()

with open(file_name, 'w') as files:
    files.write(f'\n{data}')

# Использование with для работы с файлами имеет несколько преимуществ:
# 1. Автоматическое закрытие файла: После выхода из блока with файл автоматически закрывается, даже если произошло
# исключение. Это помогает избежать утечек ресурсов и гарантирует, что файл всегда будет корректно закрыт.
# 2. Более чистый и компактный код: Использование with делает код более читабельным и компактным, так как нет
# необходимости вручную вызывать метод close() для закрытия файла.

value_1 = input()
value_2 = input()
file_1 = 'doc/fileX.txt'
file_2 = 'doc/fileX2.txt'
file_3 = 'doc/fileX3.txt'


with open(file_1, 'w', encoding='utf-8') as f_1, open(file_2, 'w', encoding='utf-8') as f_2:
    f_1.write(f'{value_1}')
    f_2.write(f'{value_2}')

with open(file_3, 'w', encoding='utf-8') as f_3:
    with open(file_1, 'r', encoding='utf-8') as f_1:
        file_1_content = f_1.read()
    with open(file_2, 'r', encoding='utf-8') as f_2:
        file_2_content = f_2.read()
    f_3.write(f'{file_1_content}\n{file_2_content}')

with open(file_3, 'r', encoding='utf-8') as files:
    content = files.read()
    print(content)