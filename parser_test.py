import const
from bs4 import BeautifulSoup
from utils import openFile, createSoup, getSoup, get_by_name, get_by_team, printResults
from requests import getItems

def main():
    choice = int(input('1-все результаты по ФИО, 2-все результаты гонок по команде, 3-завершить:'))
    path_list = [const.PATH_TO_HTML1, const.PATH_TO_HTML2, const.PATH_TO_HTML3, const.PATH_TO_HTML4, const.PATH_TO_HTML5, const.PATH_TO_HTML6, const.PATH_TO_HTML7, const.PATH_TO_HTML8, const.PATH_TO_HTML9, const.PATH_TO_HTML10, const.PATH_TO_HTML11, const.PATH_TO_HTML12, const.PATH_TO_HTML13, const.PATH_TO_HTML14, const.PATH_TO_HTML15, const.PATH_TO_HTML16, const.PATH_TO_HTML17, const.PATH_TO_HTML18, const.PATH_TO_HTML19, const.PATH_TO_HTML20, const.PATH_TO_HTML21, const.PATH_TO_HTML22, const.PATH_TO_HTML23, const.PATH_TO_HTML24]

    while choice != '3':
        if choice == '1':
            name = input('Введите имя, чтобы выдать результаты всех гонок):')
            for path in path_list:
                printResults(path, name, option='by_name')
        elif choice == '2':
            team = input('Введите команду, чтобы выдать результаты всех гонок):')
            for path in path_list:
                printResults(path, team, option='by_name')
        else:
            pass # заглушка; в будущем добавить хендлер для обработки
        
        choice = int(input('1-все результаты по ФИО, 2-все результаты гонок по команде, 3-завершить:'))
    

if __name__ == '__main__':
    main()
