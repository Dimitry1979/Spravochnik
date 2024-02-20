from data_create import name_data, surname_data, phone_data, address_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(
        f'В каком формате внести данные?\n\n1 вариант:\n{name}\n{surname}\n{phone}\n{address}\n'
        f'2 вариант: \n{name};{surname};{phone};{address}\n Сделайте выбор: '))
    while var != 1 and var != 2:
        print('Неправильный выбор')
        var = int(input('Сделайте выбор: '))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
            return f'{name}\n{surname}\n{phone}\n{address}\n\n'
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.write(f'{name};{surname};{phone};{address}\n')
            return f'{name};{surname};{phone};{address}\n'


def read_data():
    command = int(input('В каком формате вывести данные(1/2): '))

    while command != 1 and command != 2:
        print('Неправильный выбор')
        command = int(input('Сделайте выбор: '))

    if command == 1:
        print('Read data from first file: \n')
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            data_first_list = []
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == "\n" or i == len(data_first) - 1:
                    data_first_list.append(''.join(data_first[j:i + 1]))
                    j = i
            print(''.join(data_first_list))
            return data_first
    elif command == 2:
        print('Read data from second file: \n')
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = f.readlines()
            print(*data_second)
            return data_second


def change_data():
    data_list = read_data()
    name_data_d = input('Введите название данных, которые вы хотите изменить: ')
    number_file = int(input('Введите из какого файла вы хотите внести изменения(1/2): '))
    while number_file != 1 and number_file != 2:
        print('Неправильный ввод')
        number_file = int(input('Введите из какого файла вы хотите внести изменения(1/2): '))
    if number_file == 1:
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            for i in range(len(data_list)):
                if str(data_list[i]).startswith(name_data_d):
                    for j in range(i):
                        f.write(data_list[j])
                    data_list[i] = input_data()
                    f.write(data_list[i])
                    for k in range(i + 5, len(data_list) - 1):
                        f.write(data_list[k])

    elif number_file == 2:
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            for i in range(len(data_list)):
                if str(data_list[i]).startswith(name_data_d):
                    f.write(str(*data_list[:i]))
                    data_list[i] = input_data()
                    f.write(str(data_list[i]))
                    f.write(str(*data_list[i+1:]))


def delete_data():
    data_list = read_data()
    name_data_d = input('Введите название данных, которые вы хотите удалить: ')
    number_file = int(input('Введите, из какого файла вы хотите удалить данные(1/2): '))
    while number_file != 1 and number_file != 2:
        print('Неправильный ввод')
        number_file = int(input('Введите, из какого файла вы хотите удалить данные(1/2): '))
    if number_file == 1:
        with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
            for i in range(len(data_list)):
                if str(data_list[i]).startswith(name_data_d):
                    for j in range(i):
                        f.write(data_list[j])
                    for k in range(i + 5, len(data_list) - 1):
                        f.write(data_list[k])
    elif number_file == 2:
        with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
            for i in range(len(data_list)):
                if str(data_list[i]).startswith(name_data_d):
                    f.write(str(*data_list[:i]))
                    f.write(str(*data_list[i + 1:]))