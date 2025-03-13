# словарь, dict (ключ: значение)
family = {
    'Dad': 'Alex',
    'Mom': 'Olga',
    'Son': 'Simon',
    'Daughter': 'Anna'
}
print(f'Dict value - {family["Dad"]}')
print(f'Dict value - {family.get("Dad")}')
for key, value in family.items():
    print(f'Key - {key}, Value - {value}')

family_list = [['Dad', 'Vlad'], ['Mom', 'Mary']]
family_2 = dict(family_list)
print(f'Family 2 - {family_2}')

person = {
    "name": 'Alex',
    "age": 30,
    "city": 'SPB'
}
print(f'Dict person - {person}')

person["email"] = 'alex@mail.ru'  # добавление данных
print(f'Email added - {person}')

person["email"] = 'alex_stepik@mail.ru'  # изменение данных
print(f'Email replaced - {person}')

del person['city']  # удаление данных
print(f'City deleted - {person}')

keys = person.keys() # получение ключей
print(f'Person keys - {keys}')

for key in person.keys():
    print(f'Key - {key}')

if "name" in person.keys():
    print("Key exists")

values = person.values() # получение значений
print(f'Person values - {values}')

for values in person.values():
    print(f'Values - {values}')

if "Alex" in person.values():
    print("Value exists")