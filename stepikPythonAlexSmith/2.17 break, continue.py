list = [1, 4, 6, 10, 12]
for i in list:
    if i == 6:
        print('Its 6')
        break
    print(i)

# login = input('Your login: ')
# while True:
#     if login == 'Alex':
#         print('Ok')
#         password = input('Your password: ')
#     else:
#         print('Not Ok')
#         break

for i in list:
    if i == 10:
        print('Its 10')
        break
    elif i == 4:
        print('Its 4')
    elif i == 6:
        print('Its 6')
        continue
    print(i)