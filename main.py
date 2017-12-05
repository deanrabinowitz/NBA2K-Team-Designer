from solver import player_solver, team_solver
from player_creator import create_random_players
from random import choice

POSITIONS = ["PG", "SG", "SF", "PF", "C"]

players = {position: create_random_players(100) for position in POSITIONS}
attribute_bounds = {
    "3pt": (8, 10),
    "close_range": (3, 10),
    "rebounds": (1, 5)
}
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
