from solver import player_solver, team_solver, harden_constraints
from data_processor import get_player_lists
from random import choice
import json
from pprint import pprint

POSITIONS = ["PG", "SG", "SF", "PF", "C"]
ATTRIBUTES = ['inside', 'outside', 'playmaking',
              'athleticism', 'defense', 'rebounding']

def team_printer(satisfactory_team):

    #Logical order when naming positions
    order = ['PG', 'SG', 'SF', 'PF', 'C']

    for position in order:
        print("Position: ", position)
        print("\tName:", satisfactory_team[position]['player']['name'])
        print("\tOverall:", str(satisfactory_team[position]['player']['overall']) + 'th', 'percentile')
        print("\tAthleticism:", str(satisfactory_team[position]['player']['athleticism']) + 'th', 'percentile')
        print("\tDefense:", str(satisfactory_team[position]['player']['defense']) + 'th', 'percentile')
        print("\tInside:", str(satisfactory_team[position]['player']['inside']) + 'th', 'percentile')
        print("\tOutside:", str(satisfactory_team[position]['player']['outside']) + 'th', 'percentile')
        print("\tPlaymaking:", str(satisfactory_team[position]['player']['playmaking']) + 'th', 'percentile')
        print("\tRebounding:", str(satisfactory_team[position]['player']['rebounding']) + 'th', 'percentile')
        print()


########################### INITIALIZE PLAYER DICTS ###########################

player_lists = get_player_lists()

########################### INITIALIZE CONSTRAINTS ############################

json_file = open("team_constraints.json")
json_str = json_file.read()
soft_constraints = json.loads(json_str)

############################### SOLVE PLAYERS #################################

satisfactory_players = {}

for position in POSITIONS:
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
    team_printer(choice(satisfactory_teams))
