letters = ['a', 'b', 'c']


class TicTacToe:
    def __init__(self):
        self.turn = 'X'
        self.positions = [f'{letter}{number}' for letter in letters for number in range(1, 4)]
        self.taken_positions = []

    def mark_square(self):
        pass

    def check_if_won(self):
        pass

