import const
from bs4 import BeautifulSoup
from utils import *
from requests import getItems

#Александр Большунов

def main():
    way = [const.PATH_TO_HTML1, const.PATH_TO_HTML2, const.PATH_TO_HTML3, const.PATH_TO_HTML4, const.PATH_TO_HTML5, const.PATH_TO_HTML6, const.PATH_TO_HTML7, const.PATH_TO_HTML8, const.PATH_TO_HTML9, const.PATH_TO_HTML10, const.PATH_TO_HTML11, const.PATH_TO_HTML12, const.PATH_TO_HTML13, const.PATH_TO_HTML14, const.PATH_TO_HTML15, const.PATH_TO_HTML16, const.PATH_TO_HTML17, const.PATH_TO_HTML18, const.PATH_TO_HTML19, const.PATH_TO_HTML20, const.PATH_TO_HTML21, const.PATH_TO_HTML22, const.PATH_TO_HTML23, const.PATH_TO_HTML24]
    for path in way:
        printResults(path)

if __name__ == '__main__':
    main()  