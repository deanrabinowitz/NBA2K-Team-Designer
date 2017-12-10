from solver import player_solver, team_solver
from data_processor import get_player_lists
from random import choice

POSITIONS = ["PG", "SG", "SF", "PF", "C"]
ATTRIBUTES = ['inside', 'outside', 'playmaking',
              'athleticism', 'defense', 'rebounding']

########################### INITIALIZE PLAYER DICTS ###########################

player_lists = get_player_lists()

########################### INITIALIZE CONSTRAINTS ############################



solution_players = {position: player_solver(players[position], attribute_bounds) for position in POSITIONS}
for position, player_list in solution_players.items():
    for index, player in enumerate(player_list):
        player_list[index] = player["player"]

solution_teams = team_solver(solution_players, 200)
team = choice(solution_teams)
team_overall = 0
for player in team.values():
    team_overall += player["overall"]

print(team_overall)
print(len(solution_teams))
print(team)
