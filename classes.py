class Player:
    def __init__(self, name, level, active):
        self.name = name
        self.level = level
        self.active = active
class Team:
    global global_team_number
    global_team_number = 0
    def __init__(self, list_players=[], total_level=0, number_players=0):
        self.list_players = list_players
        self.total_level = total_level
        self.number_players = number_players
        self.name = ''
        global global_team_number
        self.team_number = global_team_number + 1        
        global_team_number +=1
    def add_player (self,player):
        if(self.number_players==0):
            self.name = 'Команда ' + str(self.team_number)#+ player.name
        self.list_players.append(player)
        self.total_level = self.total_level + player.level
        self.number_players += 1        