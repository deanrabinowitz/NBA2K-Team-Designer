import numpy as np
import matplotlib.pyplot as plt


def graph(formula, x):
    y = formula(x)
    plt.plot(x, y)
    print("see plot")
    plt.show()


def games_played_factor(x):
    return (x/1)**(1/3)


def three_point_stat(player):
    attempt_rate = player['3PAr']
    points_attempted = player['3PA']
    percentage = player['3P%']
    games_played_factor = (player['G']/82)**(1/3)
    advanced_factor = .25
    raw_factor = 1 - advanced_factor
    raw_1 = .6
    raw_2 = .4

    return games_played_factor * (advanced_factor * attempt_rate + raw_factor *
                                  (raw_1 * points_attempted + raw_2 * percentage * 10)
                                  )

# graph(games_played_factor, np.arange(0.01, 1.01, 0.01))

curry = {"name": "Stephen Curry",
         "G": 79,
         "3PAr": .547,
         "3PA": 10.0,
         "3P%": .411}

harden = {"name": "James Harden",
          "G": 81,
          "3PAr": .493,
          "3PA": 9.3,
          "3P%": .347}

gordon = {"name": "Eric Gordon",
          "G": 75,
          "3PAr": .651,
          "3PA": 8.8,
          "3P%": .372}

gasol = {"name": "Pau Gasol",
          "G": 64,
          "3PAr": .172,
          "3PA": 1.6,
          "3P%": .538}

print("Curry 3: {}".format(three_point_stat(curry)))
print("Harden 3: {}".format(three_point_stat(harden)))
print("Gordon 3: {}".format(three_point_stat(gordon)))
print("Gasol 3: {}".format(three_point_stat(gasol)))
