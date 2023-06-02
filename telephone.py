import os

data = 'tel.txt'
columns = ['Фамилия' , 'Имя' , 'Телефон']

def ReadFile(data: str): # Функция выгрузки данных в файл
    newdata = []
    with open(data, 'r', encoding='utf-8') as f:
        for line in f:
            record = dict(zip(columns, line.strip().split(',')))
            newdata.append(record)
    return newdata

def SaveData(data, newdata):
     with open(data, 'w', encoding='utf-8')as f:
        for i in range(len(newdata)):
            s=''
            for v in newdata[i].values():
                s+= v + ','
            f.write(f'{s[:-1]}\n')
        print('Данные обновлены')

def PrintIdent(): # Вывод на экран разделителя (для лучшей читаемости в консоли)
    print()
    for i in range(20):
        print('_', end='')

def PrintData(): # Вывод всех данных на экран (0)
    newdata = ReadFile(data)
    number = 0
    PrintIdent()
    print('Данные справочника:')
    for i in newdata:
        number += 1
        print(f'{number}', end = '. ')
        print(*i.values())

def Search(): # Меню поиска
    while True:
        PrintIdent()
        print('Меню поиска')
        for i in range(len(columns)):
            print(f'{i} - поиск по полю {columns[i]}')
        print(f'{len(columns)} - выход в главное меню')
        answer = int(input('Введите номер меню: '))
        if answer == len(columns): break
        if 0 <= answer <len(columns):
            searched = input('Введите искомое значение')
            SearchData(searched, answer)

def SearchData(searchedData, fieldNumber): # Функция поиска по полю (1)
    phoneDirectory = ReadFile(data)
    tick = 0
    PrintIdent()
    print('Результаты поиска: ')
    for line in phoneDirectory:
        i += 1
        if searchedData.lower() in line[columns[fieldNumber]].lower:
            find = True
            print(f'{i}', end=" ")
            print(*line.values())
    if find == False: print(f'{searchedData} не найдена')

def NewPerson(): # Добавление нового пользователя (2)
    phoneDirectory = ReadFile(data)
    newRecord = dict()
    for i in range(len(columns)):
        newRecord[columns[i]]=(input(f'Введите данные по полю "{columns[i]}": '))
    phoneDirectory.append(newRecord)
    SaveData(data, phoneDirectory)

def Edit(): # меню изменения записи (3)
    PrintData()
    Index = int(input('Введите номер редактируемой записи: '))-1
    print(*enumerate(columns))
    fieldsIndex = int(input('Введите номер поля для редактирования: '))
    phoneDirectory = ReadFile(data)
    phoneDirectory[Index][columns[fieldsIndex]] = input('Введите новые данные: ')
    SaveData(data, phoneDirectory)

def Delete(): #Удаление записи по введенному индексу
    PrintData()
    recIndex = int(input('Введите номер удаляемой записи: '))-1
    phoneDirectory = ReadFile(data)
    phoneDirectory.pop(recIndex)
    SaveData(data, phoneDirectory)


def main():
    while True:
        PrintIdent()
        print('Главное меню:')
        print('0 - вывести все данные')
        print('1 - войти в меню поиска')
        print('2 - ввести новую запись')
        print('3 - Редактировать запись из справочника')
        print('4 - удалить запись из справочника')
        print('5 - выйти из программы')
        print('Что вы хотите сделать?')
        my_choice = int(input())
        if my_choice == 5:
            print('До свидания!')
            return
        elif my_choice == 0:
            PrintData()
        elif my_choice == 1:
            Search()
        elif my_choice == 2:
            NewPerson()
        elif my_choice == 3:
            Edit()
        elif my_choice == 4:
            Delete()
        
        


if __name__ == '__main__':
    main()