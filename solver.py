from constraint import Problem

def player_solver(players, attribute_bounds):

    def create_constraint(attribute, bounds):
        min_value, max_value = bounds
        def constraint(player):
            return max_value >= player[attribute] >= min_value
        return constraint

    problem = Problem()
    problem.addVariable("player", players)

    for attribute, bounds in attribute_bounds.items():
        constraint = create_constraint(attribute, bounds)
        problem.addConstraint(constraint, ["player"])

    return problem.getSolutions()


def team_solver(pg, sg, pf, sf, c, token_cap):
    problem = Problem()


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
#     "name": "max",
#     "3pt": 4,
#     "mid_range": 4,
#     "close_range": 5
# }]

# constraints = {
#     "3pt": (0, 3),
#     "close_range": (3, 10)
# }

# print(player_solver(players, constraints))