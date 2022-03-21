class Player:
    def __init__(self, name, level, active):
        self.name = name
        self.level = level
        self.active = active
class Team:
    def __init__(self, list_players=[], total_level=0, number_players=0):
        self.list_players = list_players
        self.total_level = total_level
        self.number_players = number_players
        self.name = ''
    def add_player (self,player):
        if(self.number_players==0):
            self.name = player.name+"'s team"
        self.list_players.append(player)
        self.total_level = self.total_level + player.level
        self.number_players += 1        