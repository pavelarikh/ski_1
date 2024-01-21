from bs4 import BeautifulSoup

with open('/Users/pavel/Downloads/ski_1.html') as file:
    src = file.read()
    
soup = BeautifulSoup(src, 'lxml')


def out_red(text):
    print("\033[31m{}".format(text))
    
def out_yellow(text):
    print("\033[33m {}" .format(text))
    
def out_white(text):
    print("\033[37m {}" .format(text))
    
def out_blue(text):
    print("\033[34m {}" .format(text))
    

m_140124_n = soup.find_all('td', class_='table-responsive__row-item _player')
#m_140124_n[0].text.strip()

m_140124_t = soup.find_all('td', class_='table-responsive__row-item _team _tablet')
#m_140124_t[0].text.strip()

m_140124_r = soup.find_all('td', class_='table-responsive__row-item _result _tablet')
#m_140124_r[0].text.strip()

m_140124_l = soup.find_all('td', class_='table-responsive__row-item _gap')
#m_140124_l[0].text.strip()


#нужно только топ-10
amount = 0
if len(m_140124_n)>=10:
    amount = 10
elif len(m_140124_n)<10:
    amount = len(m_140124_n)
time = 1
for i in range(amount):
    print(time, out_yellow(m_140124_n[i].text.strip()), out_white(m_140124_t[i].text.strip()), out_red(m_140124_r[i].text.strip()), out_blue(m_140124_l[i].text.strip()))
    time+=1

# Я думаю сделать из этого кода функцию и по ней зделать всё для каждой гонке, просто их там много и на одной странице только одна гонка. А в баскетболе была одна страница и все результаты)
