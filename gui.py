from tkinter import *

from engine import TicTacToe


class Display:

    def __init__(self, game: TicTacToe):
        self.game = game
        self.window = Tk()
