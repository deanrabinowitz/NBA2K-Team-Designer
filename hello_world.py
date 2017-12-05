import pandas as p
import constraint as const
from Player import Player

stats = p.read_csv("playerstats.csv")
statsadvanced = p.read_csv("playerstatsadvanced.csv")

merged_stats = p.merge(left=stats, right=statsadvanced, how='outer', on='Rk')

# Define some lists.
sg_list = []
pg_list = []
sf_list = []
pf_list = []
c_list = []

positions = [sg_list, pg_list, sf_list, pf_list, c_list]
# Initialize a dataframe for each position
sg = merged_stats.loc[merged_stats.loc[:]["Pos"] == "SG"][:]
pg = merged_stats.loc[merged_stats.loc[:]["Pos"] == "PG"][:]
sf = merged_stats.loc[merged_stats.loc[:]["Pos"] == "SF"][:]
pf = merged_stats.loc[merged_stats.loc[:]["Pos"] == "PF"][:]
c = merged_stats.loc[merged_stats.loc[:]["Pos"] == "C"][:]



# Initialize a problem instance
problem = const.Problem()


# Need to create a list of player objects for each position, populate variables that way
# The commented code below will now work.

print(sg)

# it = sg.itertuples()
# row = next(it)
# while(row):
#     try:
#         player = Player()
#         player.name = row[NAME]
#         player.position = row[POS]
#         player.age = row[3]
#         player.team = row[4]
#         player.games_played = row[5]
#
#         sg_list.append(player)
#
#         row = next(it)
#         # print("name: {}\nposition: {}\nage: {}\nteam: {}\ngp: {}".format(
#         #     player.name, player.position, player.age, player.team, player.games_played))
#     except StopIteration:
#         break
# problem.addVariable("sg", sg_list)
# problem.addVariable("pg", [row for row in pg.iterrows()])
# problem.addVariable("sf", [row for row in sf.iterrows()])
# problem.addVariable("pf", [row for row in pf.iterrows()])
# problem.addVariable("c", [row for row in c.iterrows()])

