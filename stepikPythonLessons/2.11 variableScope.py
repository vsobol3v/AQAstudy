gl_1 = 100  # global
gl_2 = 20  # global


def summ1():
    global gl_1, gl_2  # изменяем глобальную переменную
    gl_1 = 30
    gl_2 = 40
    gl_result = gl_1 + gl_2  # local, доступна только здесь
    print(f'Global sum = {gl_result}')


def summ2():
    gl_result = gl_1 + gl_2  # навая local с тем же названием, доступна только здесь
    print(f'Global sum = {gl_result}')


print(f'Globals: {gl_1}, {gl_2}')
summ1()
print(f'Globals: {gl_1}, {gl_2}')
summ2()


def outer_function():
    message = "Hello, World!"

    def inner_function():
        nonlocal message
        message = "Hello, Python!"

    inner_function()
    print(message)


outer_function()  # выведет: Hello, Python!
