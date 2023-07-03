class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"Player: {self.name} Sprint: {self.sprint} Dribble: {self.dribble} Passing: {self.passing} Shooting: {self.shooting}"