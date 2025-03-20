def main():
    value_1 = input('Введите первое число: ')
    operation = input('Введите оператор: ')
    value_2 = input('Введите второе число: ')
    input_check(value_1, value_2, operation)


# Проверяем корректность ввода данных. В случае успеха запускаем соответствующую функцию.
def input_check(a, b, op):
    try:
        a = int(a)
        b = int(b)
        match op:
            case '+':
                addition(a, b)
            case '-':
                subtraction(a, b)
            case '/':
                division(a, b)
            case '*':
                multiplication(a, b)
            case _:  # если оператор не соответствует ни одному из перечисленных.
                print('Некорректный оператор')
                main()
    except ValueError:
        print('Значения должны являться целыми числами')
        main()


def addition(a, b):
    result = a + b
    print(f'Результат: {result}')
    main()


def subtraction(a, b):
    result = a - b
    print(f'Результат: {result}')
    main()


def division(a, b):
    try:
        result = a / b
        print(f'Результат: {result}')
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    main()


def multiplication(a, b):
    result = a * b
    print(f'Результат: {result}')
    main()


main()