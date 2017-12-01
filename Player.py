class Player:
    """
    This class defines any player and their associated stats.
    Should we focus on raw stats? Input the weighted stats?
    Ultimately, the constraint solver is going to access these
    values in order to determine a satisfactory team/player.
    If we do choose to do some pre-processing, and input more
    'advanced statistics' for the solver, we will have to determine
    an appropriate and realistic evaluation for the advanced stats.
    """
    def __init__(self):
        print("Created a new player")

    # All subject to change... see docstring above.
    def __slots__(self):
        self.name = None
        self.team = None
        self.position = None
        self.age = None
        self.games_played = None
        self.games_started = None
        self.minutes_per_game = None
        self.field_goal_percentage = None
        self.three_point_percentage = None
        self.effective_field_goal_percentage = None
        self.free_throw_percentage = None
        self.offensive_rebounds = None
        self.defensive_rebounds = None
        self.total_rebounds = None
        self.assists = None
        self.steals = None
        self.blocks = None
        self.turnovers = None
        self.fouls = None
        self.points = None
