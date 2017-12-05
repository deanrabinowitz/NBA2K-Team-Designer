from random import randint
from faker import Faker

fake = Faker()

ATTRIBUTES = ["close_range", "mid_range", "3pt", "assists", "rebounds", "steals", "blocks"]

def create_random_players(amount):
    players = []
    for i in range(amount):
        player = {attribute: randint(1, 10) for attribute in ATTRIBUTES}
        player["overall"] = sum(player.values())
        player["name"] = fake.name()
        players.append(player)
    return players