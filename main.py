from solver import player_solver, team_solver, harden_constraints
from data_processor import get_player_lists
from random import choice
import json
from pprint import pprint

POSITIONS = ["PG", "SG", "SF", "PF", "C"]
ATTRIBUTES = ['inside', 'outside', 'playmaking',
              'athleticism', 'defense', 'rebounding']

########################### INITIALIZE PLAYER DICTS ###########################

player_lists = get_player_lists()

########################### INITIALIZE CONSTRAINTS ############################

json_file = open("team_constraints")
json_str = json_file.read()
soft_constraints = json.loads(json_str)
# soft_constraints = {}

############################### SOLVE PLAYERS #################################

satisfactory_players = {}

for position in POSITIONS:
    # soft_constraints[position] = reify(hard_constraints[position])
    hard_constraints = harden_constraints(soft_constraints[position])
    satisfactory_players[position] = player_solver(
        player_lists[position], hard_constraints)

################################# SOLVE TEAM ##################################

print("What is the token cap? (Maximum 500)")
token_cap = int(input())

satisfactory_teams = team_solver(satisfactory_players, token_cap)

if not satisfactory_teams:
    print("No teams found, please adjust your requirements")
else:
    pprint(choice(satisfactory_teams))
