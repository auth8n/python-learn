from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        curr_move = random.choice(self.moves)
        self.position += curr_move
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    
    super().__init__().self.moves = [(x, y)]
