from bs4 import BeautifulSoup

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
    
def getItems(soup):
    rows = soup.find_all('tr', class_='table-responsive__row')
    
    result = []

    for item in rows:
        try:
            name = item.find('span', class_='table-item__name').text
            team = item.find('td', class_='_team').find('a').text

            obj = {
                'name': name,
                'team': team,
            }

            result.append(obj)
        except:
            pass

    print(result)
  
def main():
    soup = getSoup('./html/file1.html')
    getItems(soup)

if __name__ == "__main__": 
    main()