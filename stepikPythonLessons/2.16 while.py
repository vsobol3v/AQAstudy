a = 10
while a > 1:
    a -= 1
    print(a)

my_list = [1, 2, 3, 4, 5]  # Создаем список
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

fruits = ["яблоко", "банан", "апельсин", "виноград"]
index = 0
while index < len(fruits):
    if len(fruits[index]) > 7:
        print(fruits[index])
    index += 1

numbers = [1, 2, 3, 4, 5]
index = 0
while index < len(numbers):
    numbers[index] *= 2
    index += 1
print(numbers)
