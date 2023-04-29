from tkinter import *


window = Tk()
window.title('TicTacToe')
window.config(width=600, height=600, pady=20, padx=20)

grid_image = PhotoImage(file='images/grid.png')
label = Label(image=grid_image)
label.pack()

window.after(3000, window.destroy)
window.mainloop()
