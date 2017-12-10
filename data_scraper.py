import csv
import requests
from bs4 import BeautifulSoup

url = 'http://2kmtcentral.com/18/players/position/12345/collection/67-70-71-72-73-74-75-76-77-78-79-80-81-82-83-84-85-86-87-88-89-90-91-92-93-94-95-96-97-98/sort/overall'
players = []
i = 1
while True:
    page = requests.get(url)
    print('fetching page {}'.format(i-1))
    soup = BeautifulSoup(page.text, 'html.parser')
    if soup.tbody.contents == ['\n']:
        break
    rows = soup.find_all('tr')
    rows.pop(0) # get rid of table header row
    for row in rows:
        cells = [x for x in row.contents if x.name == 'td']
        player = {}
        player['name'] = cells[0].a.text
        player['overall'] = cells[1].span.text
        player['position'] = cells[2].span.text
        # player['position'] = cells[2].span.text.replace(u'\ufeff', '')
        player['inside'] = cells[3].span.text
        player['outside'] = cells[4].span.text
        player['playmaking'] = cells[5].span.text
        player['athleticism'] = cells[6].span.text
        player['defense'] = cells[7].span.text
        player['rebounding'] = cells[8].span.text
        player['height'] = cells[9].span.text
        print(player['name'])
        players.append(player)
    if i == 1:
        url = url + '/page/1'
    else:
        if i > 10:
            url = url[:-2]
        else:
            url = url[:-1]
        url = url + str(i)
    i = i + 1


with open('players.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['name', 'overall', 'position', 'inside', 'outside',
                  'playmaking', 'athleticism', 'defense', 'rebounding', 'height']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for player in players:
        writer.writerow(player)

print('we done?')
print('yeet')