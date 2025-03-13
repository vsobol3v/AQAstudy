def new_list(item):
    file_write = open('doc/shoppingList.txt', 'w', encoding='utf-8')
    file_write.write(item)
    file_write.close()
    main()


def add_item(item):
    file_add = open('doc/shoppingList.txt', 'a', encoding='utf-8')
    file_add.write(f'\n{item}')
    file_add.close()
    main()


def read_list():
    file_read = open('doc/shoppingList.txt', 'r', encoding='utf-8')
    shopping_list = file_read.read()
    file_read.close()
    print(shopping_list)
    main()


def main():
    print('Какое действие вы хотите выполнить?\n'
          '1 - Создать новый список;\n'
          '2 - Добавить позицию в список;\n'
          '3 - Просмотреть список')
    option = int(input())

    if option == 1:
        item_input = input('Введите позицию, которую вы хотите добавить: ')
        new_list(item_input)
    elif option == 2:
        item_input = input('Введите позицию, которую вы хотите добавить: ')
        add_item(item_input)
    elif option == 3:
        read_list()

    else:
        print('Нет такого действия')


main()
