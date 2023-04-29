letters = ['a', 'b', 'c']

winning_combinations = [
    ['a1', 'a2', 'a3'],
    ['b1', 'b2', 'b3'],
    ['c1', 'c2', 'c3'],
    ['a1', 'b1', 'c1'],
    ['a2', 'b2', 'c2'],
    ['a3', 'b3', 'c3'],
    ['a1', 'b2', 'c3'],
    ['c1', 'b2', 'a3']
]


class TicTacToe:
    def __init__(self) -> None:
        self.turn = 'X'
        self.empty_positions = [f'{letter}{number}' for letter in letters for number in range(1, 4)]
        self.x_positions = []
        self.o_positions = []

    def do_move(self, chosen_move: str) -> None:
        for position in self.empty_positions:
            if position == chosen_move:
                self.mark_square(position)

            if self.check_if_won():
                print(f'Player {self.turn} wins!')

            else:
                self.change_turn()

    def change_turn(self) -> None:
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def mark_square(self, position: str) -> None:
        if self.turn == 'X':
            self.x_positions.append(position)
        else:
            self.o_positions.append(position)
        self.empty_positions.remove(position)

    def check_if_won(self) -> bool:
        for combo in winning_combinations:
            if all(position in self.x_positions for position in combo):
                return True
            elif all(position in self.x_positions for position in combo):
                return True
        return False
