class Player:
    def __init__(self, token):
        self.token = token
        self.brain = HumanBrain()

    def prompt(self):
        print self.game.board.positions

        return Move(1,2,1)


