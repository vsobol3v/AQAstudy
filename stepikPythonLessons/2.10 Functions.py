def summ(num_1, num_2):
    result = num_1 + num_2
    print(result)


summ(10, 20)


def str_summ(str_1, str_2):
    result = str_1 + str_2
    print(result)


str_summ("hello", "world")
str_summ(str_2="world", str_1="hello")

name_input = input("Enter name: ")


def hi(name, age=30):
    result = f"My name is {name} Im {age}"
    return result


h = hi(name_input, 100)  # Перезапишет значение age = 30
print(h)
