from constraint import Problem

def player_solver(players, attribute_bounds):

    def create_constraint(attribute, bounds):
        min_value, max_value = bounds
        def constraint(player):
            return min_value <= player[attribute] <= max_value
        return constraint

    problem = Problem()
    problem.addVariable("player", players)

    for attribute, bounds in attribute_bounds.items():
        constraint = create_constraint(attribute, bounds)
        problem.addConstraint(constraint, ["player"])

    return problem.getSolutions()


def team_solver(all_players, max_overall):

    problem = Problem()
    for position in all_players:
        problem.addVariable(position, all_players[position])

    def constraint(pg, sg, sf, pf, c):
        team_overall = pg['overall'] + sg['overall'] + sf['overall'] + pf['overall'] + c['overall']
        return team_overall <= max_overall

    problem.addConstraint(constraint)

    return problem.getSolutions()


# players = [{
#     "name": "dean",
#     "3pt": 2,
#     "mid_range": 3,
#     "close_range": 4
# }, {
#     "name": "harland",
#     "3pt": 10,
#     "mid_range": 10,
#     "close_range": 10
# }, {
#     "name": "pekk",
#     "3pt": 4,
#     "mid_range": 4,
#     "close_range": 5
# }]

# constraints = {
#     "3pt": (0, 3),
#     "close_range": (3, 10)
# }

# print(player_solver(players, constraints))