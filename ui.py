from logger import input_data, read_data, change_data, delete_data


def interface():
    print(f'Введите Ваш выбор: \n 1: Внести данные \n 2: Вывести данные \n'
          f' 3: Изменить данные \n 4: Удалить данные \n')
    command = int(input('Cделайте выбор: '))

    while command != 1 and command != 2 and command != 3 and command != 4:
        print('Неправильный выбор')
        command = int(input('Сделайте выбор1 : '))

    if command == 1:
        input_data()
    elif command == 2:
        read_data()
    elif command == 3:
        change_data()
    elif command == 4:
        delete_data()


interface()