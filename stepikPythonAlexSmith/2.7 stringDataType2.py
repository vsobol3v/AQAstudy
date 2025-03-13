name = "Ivan"
a = "Hello {}"
result = a.format(name)
print(result)

first_name = "Ivan"
last_name = "Ivanov"
a = '{} {}'
result = a.format(first_name, last_name)
print(result)

result = f'{first_name} {last_name}'
print(result)