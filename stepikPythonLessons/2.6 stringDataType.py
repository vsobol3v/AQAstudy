var_1 = 5
var_2 = 10
result = var_1 + var_2
print("Результат: " + str(result))
print("Результат:", result)

first_name = 'Иван'
last_name = 'Петров'
full_name = first_name + ' ' + last_name
print(full_name)
print(first_name[0])
print(first_name * 3)

message = '   -hello, world!-   '
print(message.strip())  # возвращает новую строку с удаленными пробельными символами с начала и конца строки
print(message.strip('-'))  # Метод strip() также может принимать аргумент, указывающий, какие символы нужно удалить.
print(message.upper())  # upper() - используется для преобразования всех символов в строке в верхний регистр.
print(message.title())  # title() - используется для преобразования строки в "титульный регистр"

var = "12345"
print(var.isdigit())  # isdigit() -  используется для проверки, состоит ли строка исключительно из цифр.
print(dir(var))  # Функция dir() возвращает список всех методов и атрибутов, доступных для данного объекта.

text = "Hello, World"
start = text.startswith("Hel")  # startswith() - используется для проверки, начинается ли строка с указанного префикса
end = text.endswith("Hel")  # endswith() - используется для проверки, заканчивается ли строка на указанный суффикс
text_index = text.find('World')  # find() - используется для поиска подстроки в строке.
# Он возвращает индекс первого вхождения указанной подстроки, а если подстрока не найдена, возвращает значение -1.
print(start, end, text_index)

# Срезы (или "слайсы") — это мощный инструмент в Python, который позволяет извлекать подстроки из строк.
# string[start:end:step]
text = "Привет, мир!"
substring = text[0:6]
print(substring)
last_word = text[-4:]
print(last_word)
every_second_char = text[::2]
print(every_second_char)
modified_text = text[:8] + "все!"
print(modified_text)
reversed_text = text[::-1]
print(reversed_text)