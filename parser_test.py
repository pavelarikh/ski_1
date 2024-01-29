import const
from bs4 import BeautifulSoup
from utils import openFile, createSoup, getSoup
from requests import getItems

def main(path, name):
    soup = getSoup(path)
    getItems(soup)
    result = getItems(soup)
    requested = get_by_name(name, result)[0]
    print(f'{requested['compition']}:')
    print(f'{requested['rank']} {requested['name']} {requested['team']} {requested['result_']} {requested['gap']}')

def main_1(path, team):
    soup = getSoup(path)
    getItems(soup)
    result = getItems(soup)
    requested = get_by_team(team, result)[0]
    print(f'{requested['compition']}:')
    print(f'{requested['rank']} {requested['name']} {requested['team']} {requested['result_']} {requested['gap']}')


answer = int(input('1-все результаты по ФИО, 2-все результаты гонок по команде:'))
way = [const.PATH_TO_HTML1, const.PATH_TO_HTML2, const.PATH_TO_HTML3, const.PATH_TO_HTML4, const.PATH_TO_HTML5, const.PATH_TO_HTML6, const.PATH_TO_HTML7, const.PATH_TO_HTML8, const.PATH_TO_HTML9, const.PATH_TO_HTML10, const.PATH_TO_HTML11, const.PATH_TO_HTML12, const.PATH_TO_HTML13, const.PATH_TO_HTML14, const.PATH_TO_HTML15, const.PATH_TO_HTML16, const.PATH_TO_HTML17, const.PATH_TO_HTML18, const.PATH_TO_HTML19, const.PATH_TO_HTML20, const.PATH_TO_HTML21, const.PATH_TO_HTML22, const.PATH_TO_HTML23, const.PATH_TO_HTML24]

if answer==1:
    name = input('Введите имя, чтобы выдать результаты всех гонок):')
    for i in range(len(way)):
        try:
            main(way[i], name)
        except:
            pass
elif answer==2:
    team = input('Введите команду, чтобы выдать результаты всех гонок):')
    for i in range(len(way)):
        try:
            main_1(way[i], team)
        except:
            pass
