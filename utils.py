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

def get_by_game(results):
    finded = []

    for result in results:
        finded.append(result)

    return finded

def printResults(path, key, option='by_name'):
    soup = getSoup(path)
    getItems(soup)
    result = getItems(soup)
    
    if option == 'by_name':
        requested = get_by_name(key, result)[0]
        if len(requested['gap']) > 0:
            print(f"Команда: {requested['team']} Место: {requested['rank']} Название: {requested['compition']} Отставание: {requested['gap']} Результат: {requested['result_']}")
        else:
            print(f"Команда: {requested['team']} Место: {requested['rank']} Название: {requested['compition']} Результат: {requested['result_']}")
    elif option == 'by_team':
        requested = get_by_team(key, result)
        for item in requested:
            print(f"{item['rank']} {item['name']} {item['team']} {item['result_']} {item['gap']}")
    elif option == 'by_game':
        get_by_game(result)
    else:
        pass # заглушка; в будущем здесь будем вызывать ошибку