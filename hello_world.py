import pandas as p
import constraint as const
from Player import Player


############################### Data Scraping #################################

stats = p.read_csv("playerstats.csv", index_col=False)
statsadvanced = p.read_csv("playerstatsadvanced.csv", index_col=False)
merged_stats = p.merge(left=stats, right=statsadvanced, how='outer',
                       on=['Rk', 'Player', 'Pos', 'Age', 'Tm', 'G', 'MP'])


############################## Data Processing ################################

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


it = sg.itertuples()
row = next(it)
while row:
    try:
        player = Player()
        player.name = row[2].split("\\")[0]
        player.position = row[3]
        player.age = row[4]
        player.team = row[5]
        player.games_played = row[6]

        sg_list.append(player)

        row = next(it)
        print("name: {}\nposition: {}\nage: {}\nteam: {}\ngp: {}".format(
            player.name, player.position, player.age, player.team, player.games_played))
    except StopIteration:
        print("stopped it")
        break
