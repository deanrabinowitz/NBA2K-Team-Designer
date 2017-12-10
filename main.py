from solver import player_solver, team_solver, reify
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
hard_constraints = json.loads(json_str)
# soft_constraints = {}

############################### SOLVE PLAYERS #################################

satisfactory_players = {}

for position in POSITIONS:
    # soft_constraints[position] = reify(hard_constraints[position])
    soft_constraints = reify(hard_constraints[position])
    satisfactory_players[position] = player_solver(
        player_lists[position], soft_constraints)

################################# SOLVE TEAM ##################################

print("What is the token cap? (Maximum 500)")
token_cap = int(input())

satisfactory_teams = team_solver(satisfactory_players, token_cap)

pprint(satisfactory_teams)

# solution_players = {position: player_solver(players[position], attribute_bounds) for position in POSITIONS}
# for position, player_list in solution_players.items():
#     for index, player in enumerate(player_list):
#         player_list[index] = player["player"]
#
# solution_teams = team_solver(solution_players, 200)
# team = choice(solution_teams)
# team_overall = 0
# for player in team.values():
#     team_overall += player["overall"]
#
# print(team_overall)
# print(len(solution_teams))
# print(team)
