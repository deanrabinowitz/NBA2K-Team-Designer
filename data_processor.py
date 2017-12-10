import csv
from scipy.stats import percentileofscore as percentile

POSITIONS = ['PG', 'SG', 'SF', 'PF', 'C']
ATTRIBUTES = ['overall', 'inside', 'outside', 'playmaking',
              'athleticism', 'defense', 'rebounding']


def get_player_lists():
    position_attribute_scores = {position: {} for position in POSITIONS}
    player_lists = {position: [] for position in POSITIONS}

    for position in position_attribute_scores:
        for attribute in ATTRIBUTES:
            position_attribute_scores[position][attribute] = []

    with open('players.csv', mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for player_row in reader:
            for attribute in ATTRIBUTES:
                score = int(player_row[attribute])
                position = player_row['position']
                position_attribute_scores[position][attribute].append(score)

    with open('players.csv', mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for player_row in reader:
            player = {}
            position = player_row['position']
            player['name'] = player_row['name']
            player['position'] = position
            for attribute in ATTRIBUTES:
                player_score = int(player_row[attribute])
                scores = position_attribute_scores[player_row['position']][attribute]
                player[attribute] = percentile(scores, player_score, 'weak')

            player_lists[position].append(player)

    return player_lists

my_list = get_player_lists()
print(my_list["PG"][0])