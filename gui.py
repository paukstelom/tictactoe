from tkinter import *


class Display:

    def __init__(self):
        self.game = None
        self.setup_display()
        self.buttons = []

    def setup_display(self):
        window = Tk()
        window.title('TicTacToe')
        window.config(pady=20, padx=20)
        grid_image = PhotoImage(file='images/grid.png')
        canvas = Canvas(width=600, height=600)
        canvas.create_image(300, 300, image=grid_image)
        canvas.grid(row=1, column=1)
        window.after(3000, window.destroy)
        window.mainloop()


