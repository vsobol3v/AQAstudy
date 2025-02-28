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

# Проверка, явлеется ли число простым.
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def print_primes(numbers):
    index = 0
    while index < len(numbers):
        if is_prime(numbers[index]):
            print(numbers[index])
        index += 1


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print_primes(numbers)
