from bs4 import BeautifulSoup
from requests import getItems

def openFile(path):
    with open(path) as file:
        src = file.read()
    return src

def createSoup(file):
    soup = BeautifulSoup(file, 'lxml')
    return soup

def getSoup(path):
    file = openFile(path)
    soup = createSoup(file)
    return soup

def get_by_name(name, results):
    finded = []
    
    print('hhh', results)
    
    for result in results:
        if result['name'] == name:
            finded.append(result)
     
    return finded

def get_by_team(team, results):
    finded = []

    for result in results:
        if result['team'] == team:
             finded.append(result)

    return finded

def printResults(path):
    soup = getSoup(path)
    getItems(soup)
    result = getItems(soup)
    
    choice = input('1-все результаты по ФИО, 2-все результаты гонок по команде, 3-результаты гонки по названию и дате, 4-результаты всех гонок, 5-завершить\n')    
    
    while choice != '5':
        if choice == '1':
            key = input('Введите имя, чтобы выдать результаты всех гонок):\n')
            get_by_name(key, result)
            #requested = get_by_name(key, result)[0]
        elif choice == '2':
            key = input('Введите команду, чтобы выдать результаты всех гонок):\n')
            requested = get_by_team(key, result)[0]
        elif choice == '3':
            pass # в будущем функция определиния результата по названию гонке и дате
        elif choice == '4':
            pass # в будущем вывод топ-3 всех гонок 
        else:
            pass # заглушка; в будущем здесь будем вызывать ошибку
    
        print(f'{requested['rank']} {requested['name']} {requested['team']} {requested['result_']} {requested['gap']}')