n = 'Alex'
a = 30


def description(name, age, sex):
    print(f'{name}, {age}, {sex}')


description('Mary', 28, 'female')  # позиционный аргумент
description(name='Vlad', sex='male', age=28)  # именованный аргумент
description(n, a, 'male')


def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


greet("Alex")
greet("Anna", "Goodbye")
greet(name="Olga")
greet(greeting="Hi", name="Roman")


def new_function(value):
    numbers = list(value.split())
    unique = []
    for i in range(len(numbers)):
        if numbers[i] not in unique:
            unique.append(numbers[i])
    for j in unique:
        print(j)


new_function(input())