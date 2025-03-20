# a = int(input('Введите первое значение: '))
# b = int(input('Введите второе значение: '))

a = 5
b = 0

try:
    result = int(a / b)
    print(f'Результат: {result}')
except ZeroDivisionError:
    result = 0
    print('На 0 делить нельзя')
finally:   # блок выполняется вcегда, даже если будет выполнен except
    print("До скорых встреч")