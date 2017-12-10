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


def reify(soft_constraints):
    bounds = {"poor": (0, 20), "fair": (21, 40), "average": (41, 60),
              "good": (61, 80), "excellent": (81, 100)}
    hard_constraints = {}
    for attribute, value in soft_constraints.items():
        hard_constraints[attribute] = bounds.get(value)

    return hard_constraints
