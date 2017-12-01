import pandas as p
import constraint as const

stats = p.read_csv("playerstats.csv")

# Initialize a dataframe for each position
sg = stats.loc[stats.loc[:]["Pos"] == "SG"][:]
pg = stats.loc[stats.loc[:]["Pos"] == "PG"][:]
sf = stats.loc[stats.loc[:]["Pos"] == "SF"][:]
pf = stats.loc[stats.loc[:]["Pos"] == "PF"][:]
c = stats.loc[stats.loc[:]["Pos"] == "C"][:]

# Initialize a problem instance
problem = const.Problem()


# Need to create a list of player objects for each position, populate variables that way
# The commented code below will now work.

# problem.addVariable("sg", [row for row in sg.iterrows()])
# problem.addVariable("pg", [row for row in pg.iterrows()])
# problem.addVariable("sf", [row for row in sf.iterrows()])
# problem.addVariable("pf", [row for row in pf.iterrows()])
# problem.addVariable("c", [row for row in c.iterrows()])

