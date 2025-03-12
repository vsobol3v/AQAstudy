# множества, set
family = {'Alex', 'Olga', 'Simon', 'Nasta', 'Alex'}
print(f'Family set - {family}')  # выведет только уникальные значения в случайном порядке

colors_list = ["red", "green", "blue"]
colors = set(colors_list)
print(f'Colors set - {colors}')

colors.add("yellow")    # Добавление нового элемента
print(f'Color added - {colors}')

colors.remove("yellow")  # Удаление элемента
print(f'Color deleted - {colors}')

colors_1 = {"red", "green", "blue"}
colors_2 = {"yellow", "green", "blue"}

print(f'Join - {colors_1 | colors_2}')  # объединение, остаются только уникальные элементы
# result = colors_1.union(colors_2) - аналогично

print(f'Intersection - {colors_1 & colors_2}')  # Пересечение, остаются элементы из обоих множеств
# result = colors_1.intersection(colors_2) - аналогично

print(f'Difference - {colors_1 - colors_2}')  # Разность, результат, который содержится в первом множестве,
# но отсутствует во втором множестве
# result = colors_1.difference(colors_2) - аналогично

print(f'Symmetric difference - {colors_1 ^ colors_2}')  #Симметрическая разность - вывод элементов из первого и второго
# множества, за вычетом дублей
# result = colors_1.symmetric_difference(colors_2) - аналогично