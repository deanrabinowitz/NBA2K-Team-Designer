import csv
from scipy.stats import percentileofscore as percentile


def init():
    attributes = ['overall', 'inside', 'outside', 'playmaking', 'athleticism', 'defense',
                  'rebounding']
    position_attribute_scores = {"PG": {},
                                 "SG": {},
                                 "SF": {},
                                 "PF": {},
                                 "C": {}}
    player_lists = {"PG": [],
                    "SG": [],
                    "SF": [],
                    "PF": [],
                    "C": []}

    for position in position_attribute_scores:
        for attribute in attributes:
            position_attribute_scores[position][attribute] = []

    with open('players.csv', mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for player_row in reader:
            for attribute in attributes:
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
            for attribute in attributes:
                player_score = int(player_row[attribute])
                scores = position_attribute_scores[player_row['position']][attribute]
                player[attribute] = percentile(scores, player_score, 'rank')
                player_lists[position].append(player)

    return player_lists


players = init()
print(players['PG'][0])