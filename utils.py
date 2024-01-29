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

def printResults(path, key, option='by_name'):
    soup = getSoup(path)
    getItems(soup)
    result = getItems(soup)
    
    if option == 'by_name':
        requested = get_by_name(key, result)[0]
        print(f"Команда: {requested['team']} Место: {requested['rank']}")
    elif option == 'by_team':
        requested = get_by_team(key, result)[0]
        #print(f"{requested['rank']} {requested['name']} {requested['team']} {requested['result_']} {requested['gap']}")
    else:
        pass # заглушка; в будущем здесь будем вызывать ошибку
