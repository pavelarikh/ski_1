from bs4 import BeautifulSoup

PATH_TO_HTML1 = '/Users/pavel/Downloads/PATH_TO_HTML1.html'
PATH_TO_HTML2 = '/Users/pavel/Downloads/PATH_TO_HTML2.html'
PATH_TO_HTML3 = '/Users/pavel/Downloads/PATH_TO_HTML3.html'
PATH_TO_HTML4 = '/Users/pavel/Downloads/PATH_TO_HTML4.html'
PATH_TO_HTML5 = '/Users/pavel/Downloads/PATH_TO_HTML5.html'
PATH_TO_HTML6 = '/Users/pavel/Downloads/PATH_TO_HTML6.html'
PATH_TO_HTML7 = '/Users/pavel/Downloads/PATH_TO_HTML7.html'
PATH_TO_HTML8 = '/Users/pavel/Downloads/PATH_TO_HTML8.html'
PATH_TO_HTML9 = '/Users/pavel/Downloads/PATH_TO_HTML9.html'
PATH_TO_HTML10 = '/Users/pavel/Downloads/PATH_TO_HTML10.html'
PATH_TO_HTML11 = '/Users/pavel/Downloads/PATH_TO_HTML11.html'
PATH_TO_HTML12 = '/Users/pavel/Downloads/PATH_TO_HTML12.html'
PATH_TO_HTML13 = '/Users/pavel/Downloads/PATH_TO_HTML13.html'
PATH_TO_HTML14 = '/Users/pavel/Downloads/PATH_TO_HTML14.html'
PATH_TO_HTML15 = '/Users/pavel/Downloads/PATH_TO_HTML15.html'
PATH_TO_HTML16 = '/Users/pavel/Downloads/PATH_TO_HTML16.html'
PATH_TO_HTML17 = '/Users/pavel/Downloads/PATH_TO_HTML17.html'
PATH_TO_HTML18 = '/Users/pavel/Downloads/PATH_TO_HTML18.html'
PATH_TO_HTML19 = '/Users/pavel/Downloads/PATH_TO_HTML19.html'
PATH_TO_HTML20 = '/Users/pavel/Downloads/PATH_TO_HTML20.html'
PATH_TO_HTML21 = '/Users/pavel/Downloads/PATH_TO_HTML21.html'
PATH_TO_HTML22 = '/Users/pavel/Downloads/PATH_TO_HTML22.html'
PATH_TO_HTML23 = '/Users/pavel/Downloads/PATH_TO_HTML23.html'
PATH_TO_HTML24 = '/Users/pavel/Downloads/PATH_TO_HTML24.html'

def openFile():
    with open('/Users/pavel/Downloads/PATH_TO_HTML24.html') as file:
        src = file.read()
    return src

#soup = BeautifulSoup(openFile(), 'lxml')
    
def getItems():
    name = soup.find_all('td', class_='table-responsive__row-item _player')
    #name[0].text.strip()
    
    time = soup.find_all('td', class_='table-responsive__row-item _team _tablet')
    #time[0].text.strip()

    region = soup.find_all('td', class_='table-responsive__row-item _result _tablet')
    #region[0].text.strip()

    backlog = soup.find_all('td', class_='table-responsive__row-item _gap')
    #backlog[3].text.strip()
    
    race = soup.find('div', class_='match-info__game')
    #race.text.strip()
    
    stage = soup.find('div', class_='match-info__stage')
    #stage.text.strip()
    
    date = soup.find('div', class_='match-info__title')
    #date.text.strip()
    
    number = soup.find('div', class_='match-info__title')
    #date.text.strip()
    
    time_ = 1
    for i in range(len(name)):
        print(time_, name, time)
  
def main():
    def openFile():
    soup = BeautifulSoup(openFile(), 'lxml')
    def getItems():
        
want = int(input(2 - если результат гонки))

if want==2:
    main()
