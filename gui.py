from tkinter import *

from engine import TicTacToe


class ButtonObj(Button):

    def __init__(self,
                 position: str,
                 x_image: PhotoImage,
                 o_image: PhotoImage,
                 game: TicTacToe):

        self.position = position
        self.game = game
        self.x_image = x_image
        self.o_image = o_image

        super().__init__(
            width=13,
            height=7,
            highlightthickness=0,
            bd=0,
            command=self.clicked
        )

    def clicked(self):
        if self.game.turn == 'X':
            self.config(width=145, height=145, image=self.x_image)
        else:
            self.config(width=145, height=145, image=self.o_image)
        self['state'] = 'disable'
        self.game.do_move(chosen_move=self.position)


class Display:

    def __init__(self, game: TicTacToe):
        self.game = game

        self.window = Tk()
        self.window.title('TicTacToe')
        self.window.config(pady=20, padx=20)

        self.grid_image = PhotoImage(file='images/grid.png')
        self.x_image = PhotoImage(file='images/x-button.png')
        self.o_image = PhotoImage(file='images/o-button.png')

        self.canvas = Canvas(width=600, height=600)
        self.canvas.create_image(300, 300, image=self.grid_image)
        self.canvas.grid(row=1, column=1)

        self.create_buttons()
        self.window.mainloop()

    def create_buttons(self):
        buttons = [ButtonObj(position=position,
                             game=self.game,
                             x_image=self.x_image,
                             o_image=self.o_image) for position in self.game.empty_positions]

        for button in buttons:
            letter = button.position[0]
            number = button.position[1]

            if letter == 'a':
                y = 100
            elif letter == 'b':
                y = 300
            else:
                y = 500

            if number == '1':
                x = 100
            elif number == '2':
                x = 300
            else:
                x = 500

            self.canvas.create_window(x, y, window=button)
