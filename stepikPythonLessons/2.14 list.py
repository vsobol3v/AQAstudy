personal = ["Alex", "Ivan", "Anastasia", "Olga"]
result = f"{personal[0]} {personal[2]}"
print(f"{result} - best couple")

number = [1, 15, 23, 4]
number[1] = "seven"  # изменен элемент списка
print(number)

print(len(personal))  # кол-во объектов в списке
print(personal[-1])  # последний объект в сиске
print(personal[0:2])  #диапазон до объекта НЕ включительно
print(personal[1:])  #диапазон до конца

personal.append("Fedor")  # добавляем элемент в список
print(personal)

pn = [personal, number]
print(pn)
print(pn[0][1])

# Аналогичное создание:
# pn = []
# pn.append(personal)
# pn.append(number)

fruits = ['apple', 'banana']
vegetables = ['carrot', 'potato']
combined_list = fruits + vegetables  # Конкатенация списков
print(combined_list)

fruits.extend(vegetables)  # добавление элементов одного списка в конец другого списка
print(fruits)

repeated_fruits = fruits * 2  # повторение списка
print(repeated_fruits)

print('apple' in fruits)  # Проверка принадлежности элементов в списках

fruits = ['яблоко', 'банан', 'вишня']
fruits.insert(1, 'апельсин')  # используется для вставки элемента в список по указанному индексу
print(fruits)

fruits = ['яблоко', 'банан', 'вишня', 'банан']
fruits.remove('вишня')  # удаление элемента по значению
fruits.pop(0)  # удаление элемента по индексу
print(fruits)

numbers = [5, 2, 8, 1, 9]
numbers.sort()  # сортировка чисел по возрастанию
print(numbers)

fruits = ['банан', 'яблоко', 'вишня', 'апельсин']
fruits.sort()  # сортировка строк по алфавиту
print(fruits)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_elements = sum(numbers)    # Получение суммы элементов списка
print(sum_elements)

# Метод copy() - используется для создания поверхностной копии списка. Это означает, что он создает новый список,
# содержащий те же элементы, что и оригинальный, но при этом новый список имеет свою собственную идентичность в памяти.
# Изменения в новом списке не повлияют на оригинальный список и наоборот.
original_list = [1, 2, 3]
new_list = original_list.copy()
print('До изменения нового списка:')
print('Оригинальный список:', original_list)
print('Скопированный список:', new_list)
new_list.append(4)
print('После изменения нового списка:')
print('Оригинальный список:', original_list)
print('Скопированный список:', new_list)

# Метод zip() - используется для объединения элементов из нескольких итерируемых объектов, таких как списки, кортежи или
# множества, в кортежи. Он создает итератор, который возвращает кортежи, содержащие элементы из всех переданных
# итерируемых объектов, по одному из каждого.
numbers_list = [1, 2]
str_list = ['one', 'two']
result = zip(numbers_list, str_list)
print(list(result))

numbers_list = [1, 2, 3]
str_list = ['one', 'two']
result = zip(numbers_list, str_list)
print(list(result))  # Пары образуются только для первых двух элементов первого списка.

txt = "welcome to the jungle"
x = txt.split()  # строку в список
print(x)

print('ЗАДАНИЯ')

numbers = list(map(int, '5 8 2 1 3 5 4 5 2 8 12'.split()))
num_count = []
for i in numbers:
    num_count.append(numbers.count(i))
zipped = list(zip(numbers, num_count))
print(zipped)