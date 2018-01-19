from collections import namedtuple


class Game:


    def __init__(self): # Constructeur
        self.players = [2]


    def addPlayer(self,username):
        Player = namedtuple(name=username,life=30, hand=[5])

        if self.players.length < 2:
            self.players.add[Player]




    def getPlayers(self,index):
        return self.players

