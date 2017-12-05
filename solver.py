import constraint as const

constraints = {"mid_range" : (2, 6), "close_range" : (4, 5)}

x = "close_range"

constraints[x][0] <= player.close_range <= constraints["close range"][1]
constraints["mid range"]

def player_solver(players, constraints):

    def contraint_solver(attribute, range):



    problem = const.Problem()
    problem.addVariable("p", players)


    for attribute, range in constraints.items():

        problem.addConstraint(contraint_solver(), )

    solutions = problem.getSolutions()
    return solutions


def team_solver(pg, sg, pf, sf, c, token_cap):
    problem = const.Problem()

