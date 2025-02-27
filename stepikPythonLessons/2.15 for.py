students = ['Alex', 'Ivan', 'Olga', 'Simon', 'Igor', 'Svetlana']
for f in students:
    if f == 'Olga':
        var = f'Engineer {f}'
        print(var)

for f in students[1:4]:
    print(f)

for f in students:
    print(len(f))

# Счетчик итераций
iteration = 0
for f in students:
    iteration += 1
print(f"Всего итераций: {iteration}")

fruits = ['яблоко', 'банан', 'вишня']
iteration_count = 0
for fruit in fruits:
    if "б" in fruit:
        print(f"{fruit} В данном слове есть буква 'б'")
        iteration_count += 1
print(f"Количество элементов которые содержат букву 'б': {iteration_count}")