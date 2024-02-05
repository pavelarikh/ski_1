def getItems(soup):
    rows = soup.find_all('tr', class_='table-responsive__row')

    compition = soup.find('div', class_='match-info__game').text

    result = []
    for item in rows:
        try:
            rank = item.select('td:nth-child(2)')[0].text.strip()
            name = item.find('span', class_='table-item__name').text
            team = item.find('td', class_='_team').find('a').text
            result_ = item.select('td:nth-child(5)')[0].text.strip()
            gap = item.select('td:nth-child(6)')[0].text.strip()

            obj = {
                'rank': rank,
                'name': name,
                'team': team,
                'result_': result_,
                'gap': gap,
                'compition': compition,
            }
            result.append(obj)
        except:
            pass

    return result