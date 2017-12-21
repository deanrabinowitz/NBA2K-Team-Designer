import csv
import requests
import time
from bs4 import BeautifulSoup


def fetch_players():
    url = 'http://2kmtcentral.com/18/players/position/12345/collection/67-70-71-72-73-74-75-76-77-78-79-80-81-82-83-84-85-86-87-88-89-90-91-92-93-94-95-96-97-98/sort/overall'
    players = []
    page_number = 0
    while True:
        print('fetching page {}'.format(page_number))
        page = requests.get(url)
        soup = BeautifulSoup(page.text, 'html.parser')
        print('page {} fetched'.format(page_number))
        if soup.tbody.contents == ['\n']:
            break
        player_rows = soup.find_all('tr')
         # get rid of table header row
        player_rows.pop(0)
        for player_row in player_rows:
            player = create_player(player_row) 
            players.append(player)
        if page_number == 0:
            url = url + '/page/1'
        else:
            if page_number > 9:
                url = url[:-2]
            else:
                url = url[:-1]
            url = url + str(page_number + 1)
        page_number += 1
    return players


def create_player(player_row):
    player = {}
    cells = [x for x in player_row.contents if x.name == 'td']
    player['name'] = cells[0].a.text
    player_url = cells[0].a.get('href')
    player_page = requests.get(player_url)
    soup = BeautifulSoup(player_page.text, 'html.parser')
    save_player_picture(soup)
    general_information = get_player_general_information(soup)
    attributes = get_player_attributes(soup)
    player.update(general_information)
    player.update(attributes)
    print(player['name'])
    return player


def get_player_general_information(soup):
    info = {}
    info_container = soup.find(class_='information')
    divs = info_container.find_all('div')
    print(len(divs)) # TO BE DELETED
    return info # TO BE DELETED
    position_tags = divs[1].find_all('a')
    info['primary position'] = position_tags[0].text
    if len(position_tags) > 1:
        info['secondary position'] = position_tags[1].text
    else:
        info['secondary position'] = ''
    # info['primary position'], info['secondary position'] = map(lambda tag: tag.text, position_tags)
    print(divs[3].span.text)
    info['height'] = divs[3].span.text.split()[0]
    info['weight'] = divs[4].span.text.split()[0][:-3]
    info['age'] = divs[5].span.text
    info['team'] = divs[6].span.a.text
    info['nickname'] = divs[8].span.text
    return info


def get_player_attributes(soup):
    attributes = {}
    attribute_sections = soup.find(class_='attributes-flex-container').find_all('section')

    for section in attribute_sections:
        if section == attribute_sections[-1]:
            break
        if section.h4 is not None:
            header = section.h4
            main_attribute_name = header.strong.contents[0].strip().lower()
            main_attribute_value = header.span.text
            attributes[main_attribute_name] = main_attribute_value

        attribute_list = section.ul.find_all('li')
        for attribute in attribute_list:
            attribute_name = get_attribute_name(attribute, attribute_list, section, attribute_sections)
            attribute_value = attribute.span.text
            attributes[attribute_name] = attribute_value

    return attributes


# TODO: amount of paramaters is pretty smelly here, but it is a web scraper
def get_attribute_name(attribute, attribute_list, section, attribute_sections):
    if section == attribute_sections[0] and attribute == attribute_list[-1]:
        return 'offensive consistency'
    elif section == attribute_sections[4]:
        if attribute == attribute_list[0]:
            return 'on-ball defensive iq'
        elif attribute == attribute_list[1]:
            return 'low post defensive iq'
        elif attribute == attribute_list[2]:
            return 'pick & roll defensive iq'
        elif attribute == attribute_list[3]:
            return 'help defense iq'
        elif attribute == attribute_list[-1]:
            return 'defensive consistency'

    return attribute.contents[1].strip().lower()


def save_player_picture(soup):
    pass


def write_to_csv(filename, all_players):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'overall', 'position', 'inside', 'outside',
                    'playmaking', 'athleticism', 'defense', 'rebounding', 'height']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for player in all_players:
            writer.writerow(player)


if __name__ == "__main__":
    start = time.time()
    all_players = fetch_players()
    write_to_csv('players_extended.csv', all_players)
    elapsed_time = round(time.time() - start, 2)
    print("Finished scraping data in {} seconds".format(elapsed_time))
