# Определение типа данных
x = 42
print(type(x))

y = 3.14
print(type(y))

z = "Hello, World!"
print(type(z))

if type(x) == int:
    print("Это целое число")
else:
    print("Не подходит")

if isinstance(y, int):
    print("x - является целым числом")
else:
    print("x - не является целым числом")

# Метод, который определяет, являются ли все символы строки буквами.
name = "Python"
print(name.isalpha())

# Преобразование типов
num_1 = 3.14
num_2 = int(num_1)
print(num_2)
